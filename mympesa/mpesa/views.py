import json
import requests
import base64
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Home Page View
def index(request):
    return render(request, 'index.html')

# M-Pesa STK Push Payment
@csrf_exempt
def mpesa_payment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone = data.get('phone')
            amount = data.get('amount')

            # M-Pesa API Credentials
            consumer_key = "5kjxDgZpyrOJhdYDIGrgmSUg4vG5tN2oCdumoBTkRWPoSqWv"
            consumer_secret = "X47GaqUtat7tbAGOUg83LJrt4I8qVhmgksAwjCoqVdcNidnHGchliepTsiTlO0Kk"
            business_shortcode = "174379"
            passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"  # Replace with actual passkey

            # Get Access Token
            access_token_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
            response = requests.get(access_token_url, auth=(consumer_key, consumer_secret))
            access_token = response.json().get("access_token")

            # Generate Timestamp & Password
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            password = base64.b64encode((business_shortcode + passkey + timestamp).encode()).decode()

            # STK Push API
            stk_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
            payload = {
                "BusinessShortCode": business_shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": phone,
                "PartyB": business_shortcode,
                "PhoneNumber": phone,
                "CallBackURL": "https://yourdomain.com/callback",  # Replace with your actual callback URL
                "AccountReference": "Game Payment",
                "TransactionDesc": "Pay for Game"
            }

            response = requests.post(stk_url, json=payload, headers=headers)
            return JsonResponse(response.json())

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
