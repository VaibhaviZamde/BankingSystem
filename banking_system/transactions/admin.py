from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'account', 'transaction_type', 'amount', 'timestamp', 'balance_after')
    list_filter = ('transaction_type', 'timestamp')
    search_fields = ('transaction_id', 'account__account_id', 'account__customer__username')
    date_hierarchy = 'timestamp'