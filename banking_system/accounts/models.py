from django.db import models
from core.models import User

class Account(models.Model):
    # Define ACCOUNT_TYPES at the class level (right after class definition)
    ACCOUNT_TYPES = (
        ('S', 'Savings'),
        ('C', 'Checking'),
        ('F', 'Fixed Deposit'),
    )
    
    account_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    opening_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    branch_location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.account_id} - {self.get_account_type_display()}"

class AccountRequest(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected')
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=1, choices=Account.ACCOUNT_TYPES)  # References Account's ACCOUNT_TYPES
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    requested_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    processed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='processed_requests')

    def __str__(self):
        return f"{self.customer.username} - {self.get_account_type_display()}"