# loans/forms.py
from django import forms
from .models import Loan
from core.models import Branch

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['loan_type', 'amount', 'duration_months', 'purpose', 'branch']
        widgets = {
            'loan_type': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration_months': forms.NumberInput(attrs={'class': 'form-control'}),
            'purpose': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'branch': forms.Select(attrs={'class': 'form-select'}),
        }