# Wallet Application
A Django-based wallet management application that allows users to securely manage their funds. Each user has an individual wallet where they can view their balance, add or remove funds, and view a history of all transactions. This project is designed to demonstrate user-specific wallet functionality with JWT-based authentication and secure APIs for interacting with the wallet balance and transactions.

# Features
<b>User Authentication:</b> Secure JWT-based authentication for user signup and login.</br>
<b>Wallet Management:</b> Each user has an individual wallet, initialized with a zero balance.</br>
<b>Fund Management:</b> Users can add or remove funds from their wallet.</br>
<b>Transaction History:</b> View all past transactions, including date, type (add/remove), and amount.</br>
<b>Balance Inquiry:</b> Users can check their current wallet balance via a dedicated API endpoint.</br>


# Technologies Used
<b>Backend: </b>Django 3.x, Django REST Framework (DRF)</br>
<b>Authentication:</b> JWT (JSON Web Token) for secure user access</br>
<b>Database:</b> SQLite (default for Django projects)</br>
<b>Frontend Styling:</b> Bootstrap for basic styling in templates</br>
<b>Postman:</b> For API testing</br>


# Database Models
## Wallet Model 
The Wallet model represents the user's wallet with the following fields:</br>

user: A OneToOne relationship to the User model, associating each wallet with a user.</br>
balance: Decimal field representing the current balance.</br>

## Transaction Model
The Transaction model stores each wallet transaction with the following fields:</br>

user: ForeignKey relationship to the User model.</br>
amount: Decimal field showing the amount for each transaction.</br>
transaction_type: CharField to indicate either "add" or "remove".</br>
date: DateTime field that auto-generates at the time of transaction creation.</br></br>


## JWT Authentication
This project uses JWT authentication for secure access to the APIs. JWT tokens are issued on login and must be included in the Authorization header (Bearer TOKEN) for subsequent requests. When the access token expires, a refresh token can be used to obtain a new access token.

To get tokens:

Login with the /api/token/ endpoint.</br>
Use the access token in the Authorization header for all subsequent API requests.</br>

## Screenshot of Postman Window

![Catalyst-postman](https://github.com/user-attachments/assets/06f2eaa5-c09a-40c2-868b-b299242781ab)
















