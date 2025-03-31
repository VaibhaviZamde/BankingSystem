from django.db import models
from core.models import User, Branch

class Loan(models.Model):
    LOAN_TYPES = (
        ('P', 'Personal'),
        ('H', 'Home'),
        ('E', 'Education'),
        ('B', 'Business'),
    )
    
    LOAN_STATUS = (
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
        ('D', 'Disbursed'),
        ('C', 'Closed'),
    )
    
    loan_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_customer': True})
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=1, choices=LOAN_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration_months = models.IntegerField()
    start_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='P')
    requested_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_loans')
    purpose = models.TextField()

    def __str__(self):
        return f"{self.loan_id} - {self.customer.username} - {self.get_loan_type_display()}"

class LoanPayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    principal_amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_amount = models.DecimalField(max_digits=15, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Payment for {self.loan.loan_id} - {self.amount}"