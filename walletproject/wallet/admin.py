from django.contrib import admin
from .models import Wallet,Transaction
#Register your models here.
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display=['id','user','balance']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','transaction_type','date']