 # C2B STK Push Using Django
This project demonstrates how to integrate M-Pesa STK Push (Daraja API) into a simple game using Django. The workflow ensures that users must make a payment before they can access the game.

Workflow
1️⃣ The front-end (index.html) sends a POST request containing the user's phone number and amount.

2️⃣ The Django view (mpesa_payment):

Retrieves the M-Pesa access token.
Generates a secure password for authentication.
Sends an STK Push request to the M-Pesa API.
3️⃣ M-Pesa prompts the user on their phone to approve the payment.

4️⃣ If successful, the API returns a JSON response confirming the transaction.

5️⃣ The user gains access to the game after payment is verified.

Tech Stack
Django (Backend)
HTML/CSS & JavaScript (Frontend)
M-Pesa Daraja API (Payments) 🚀
