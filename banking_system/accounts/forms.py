from django import forms
from .models import Account, AccountRequest

class AccountRequestForm(forms.ModelForm):
    class Meta:
        model = AccountRequest
        fields = ['account_type', 'initial_deposit']
        widgets = {
            'account_type': forms.Select(attrs={'class': 'form-select'}),
            'initial_deposit': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AccountCreateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_type']  # Removed 'branch' from fields
        widgets = {
            'account_type': forms.Select(attrs={'class': 'form-select'}),
        }