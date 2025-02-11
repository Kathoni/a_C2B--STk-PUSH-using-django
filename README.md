# a_C2B--STk-PUSH-using-django
Work flow of the simple game using mpesa daraja 
1The front-end (index.html) sends a POST request with phone and amount.
2The Django view:

Retrieves the access token.
Generates a secure password.
Sends an STK Push request to M-Pesa API.
3️ M-Pesa prompts the user’s phone to approve the payment.
4️ If successful, the API returns a JSON response.
5️ The user can now play the game after payment is confirmed.

