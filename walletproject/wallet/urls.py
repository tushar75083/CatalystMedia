from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('manage-funds/', views.manage_funds, name='manage_funds'),
    path('wallet-dashboard/', views.wallet_dashboard, name='wallet_dashboard'),
]
