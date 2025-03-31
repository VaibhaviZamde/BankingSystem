from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('D', 'Deposit'),
        ('W', 'Withdrawal'),
        ('T', 'Transfer'),
    )
    
    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    balance_after = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.transaction_id} - {self.get_transaction_type_display()}"