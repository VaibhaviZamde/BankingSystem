from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count
from accounts.models import Account  # Primary import
from transactions.models import Transaction
from loans.models import Loan

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html', {'user': request.user})

@login_required
def dashboard(request):
    if request.user.is_staff:
        # Staff dashboard logic
        context = {
            'total_accounts': Account.objects.count(),
            'active_loans': Loan.objects.filter(status='A').count(),
            'pending_requests': Loan.objects.filter(status='P').count(),
        }
        return render(request, 'dashboard/staff_dashboard.html', context)
    else:
        # Customer dashboard logic
        accounts = Account.objects.filter(customer=request.user, is_active=True)
        transactions = Transaction.objects.filter(account__in=accounts).order_by('-timestamp')[:5]
        loans = Loan.objects.filter(customer=request.user).order_by('-requested_at')[:3]
        
        context = {
            'accounts': accounts,
            'transactions': transactions,
            'loans': loans,
        }
        return render(request, 'dashboard/dashboard.html', context)