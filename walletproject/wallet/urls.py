from django.urls import path
from . import views

# apis
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import EnableWalletView, WalletBalanceView, UpdateBalanceView, TransactionHistoryView


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('manage-funds/', views.manage_funds, name='manage_funds'),
    path('wallet-dashboard/', views.wallet_dashboard, name='wallet_dashboard'),
    #apis
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('enable-wallet/', EnableWalletView.as_view(), name='enable_wallet'),
    path('wallet-balance/', WalletBalanceView.as_view(), name='wallet_balance'),
    path('update-balance/', UpdateBalanceView.as_view(), name='update_balance'),
    path('transaction-history/', TransactionHistoryView.as_view(), name='transaction_history'),
]
