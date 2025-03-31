from django.shortcuts import render
from accounts.models import Account  # ✅ Use the existing model

def dashboard(request):
    if request.user.is_authenticated:
        accounts = Account.objects.filter(customer=request.user, is_active=True)
    else:
        accounts = None
    return render(request, 'dashboard.html', {'accounts': accounts})
