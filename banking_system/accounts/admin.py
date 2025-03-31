from django.contrib import admin
from .models import Account, AccountRequest

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'customer', 'account_type', 'balance', 'is_active')  # Removed 'branch'
    list_filter = ('account_type', 'is_active')  # Removed 'branch' from filters
    search_fields = ('account_id', 'customer__username', 'customer__first_name', 'customer__last_name')

@admin.register(AccountRequest)
class AccountRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'account_type', 'initial_deposit', 'status', 'requested_at')
    list_filter = ('status', 'account_type')
    search_fields = ('customer__username', 'customer__first_name', 'customer__last_name')