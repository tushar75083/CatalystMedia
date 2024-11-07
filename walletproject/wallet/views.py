from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Wallet,Transaction
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import UserSignup,UserLogin
from django.contrib.auth.decorators import login_required
from decimal import Decimal, InvalidOperation

# apis
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WalletSerializer, UpdateBalanceSerializer, TransactionSerializer


# Create your views here.

def home(request):
    return render(request,'index.html')


def user_signup(request):
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            pass1=form.cleaned_data['password1']
            pass2=form.cleaned_data['password2']
            if pass1 == pass2:
                form.save()
                messages.success(request,'Successfully Registered...Now Login ...')
                return redirect('/login')
            else:
                messages.success(request,'Password Mismatch..')
                return redirect('/signup')
        else:
            messages.error(request,"Something went wrong..")
            return redirect('/signup')
    else:
        form=UserSignup()
        return render(request,'signup.html',{'form':form})
    

def user_login(request):
    # if not request.user.is_authenticated:
    if request.method == 'POST':
            form=UserLogin(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Successful Login")
                    return redirect('/profile')
                else:
                    return redirect('/signup')
            else:
                messages.error(request,'Form is not valid')
                return redirect('/login')
    else:
        form=UserLogin()
        return render(request,'login.html',{'form':form})       
    
    # else:
    #     pass


def user_logout(request):
    logout(request)
    return redirect('/')

def profile(request):
    return render(request,'profile.html')



@login_required
def manage_funds(request):
    if request.method == 'POST':
        try:
            # Convert fund_amount to Decimal
            fund_amount = Decimal(request.POST.get('fund', '0'))
            action = request.POST.get('action')
            wallet, created = Wallet.objects.get_or_create(user=request.user)  # Ensure wallet exists

            if action == 'Add':
                wallet.balance += fund_amount
                Transaction.objects.create(user=request.user, amount=fund_amount, transaction_type='add')
                messages.success(request, f"Rs.{fund_amount} added to your wallet.")
            elif action == 'Remove':
                if wallet.balance >= fund_amount:
                    wallet.balance -= fund_amount
                    Transaction.objects.create(user=request.user, amount=fund_amount, transaction_type='remove')
                    messages.success(request, f"Rs.{fund_amount} removed from your wallet.")
                else:
                    messages.error(request, "Insufficient balance.")
            else:
                messages.error(request, "Invalid action.")
            
            wallet.save()
        except (InvalidOperation, ValueError):
            messages.error(request, "Please enter a valid amount.")
        
        return redirect('wallet_dashboard')

    return render(request, 'manage_funds.html')


@login_required
def wallet_dashboard(request):
    wallet = Wallet.objects.get(user=request.user)
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    
    context = {
        'wallet': wallet,
        'transactions': transactions,
        'user_email': request.user.email
    }
    return render(request, 'wallet_dashboard.html', context)



# apis
class EnableWalletView(APIView):
    def post(self, request):
        wallet, created = Wallet.objects.get_or_create(user=request.user)
        if created:
            return Response({"message": "Wallet created and enabled."}, status=status.HTTP_201_CREATED)
        return Response({"message": "Wallet is already enabled."}, status=status.HTTP_200_OK)


class WalletBalanceView(APIView):
    def get(self, request):
        try:
            wallet = Wallet.objects.get(user=request.user)
            serializer = WalletSerializer(wallet)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found."}, status=status.HTTP_404_NOT_FOUND)


class UpdateBalanceView(APIView):
    def post(self, request):
        serializer = UpdateBalanceSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            transaction_type = serializer.validated_data['transaction_type']

            try:
                wallet = Wallet.objects.get(user=request.user)

                if transaction_type == 'add':
                    wallet.balance += amount
                elif transaction_type == 'remove':
                    if wallet.balance >= amount:
                        wallet.balance -= amount
                    else:
                        return Response({"error": "Insufficient funds."}, status=status.HTTP_400_BAD_REQUEST)

                wallet.save()

                # Create a transaction record
                Transaction.objects.create(
                    user=request.user,
                    amount=amount,
                    transaction_type=transaction_type
                )

                return Response({"message": f"Balance updated. New balance: Rs.{wallet.balance}"}, status=status.HTTP_200_OK)
            except Wallet.DoesNotExist:
                return Response({"error": "Wallet not found."}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionHistoryView(APIView):
    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user).order_by('-date')
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)