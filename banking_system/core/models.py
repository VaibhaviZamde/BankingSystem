from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # If creating a new user and no type specified, default to customer
        if not self.pk and not self.is_staff:
            self.is_customer = True
        super().save(*args, **kwargs)
        
class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_branches')
    opening_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location}"