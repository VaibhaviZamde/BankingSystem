from django.contrib import admin
from .models import Loan, LoanPayment

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'customer', 'loan_type', 'amount', 'interest_rate', 'status', 'requested_at')
    list_filter = ('loan_type', 'status', 'branch')
    search_fields = ('loan_id', 'customer__username', 'customer__first_name', 'customer__last_name')

@admin.register(LoanPayment)
class LoanPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan', 'amount', 'payment_date', 'remaining_balance')
    list_filter = ('payment_date',)
    search_fields = ('loan__loan_id', 'loan__customer__username')