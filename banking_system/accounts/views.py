from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Account, AccountRequest
from .forms import AccountRequestForm, AccountCreateForm

@login_required
def account_list(request):
    if request.user.is_customer:
        accounts = Account.objects.filter(customer=request.user, is_active=True)
    else:
        accounts = Account.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})

@login_required
def account_detail(request, account_id):
    account = get_object_or_404(Account, account_id=account_id)
    if request.user.is_customer and account.customer != request.user:
        messages.error(request, "You don't have permission to view this account.")
        return redirect('accounts:account_list')
    
    transactions = account.transactions.all().order_by('-timestamp')[:10]
    return render(request, 'accounts/account_detail.html', {
        'account': account,
        'transactions': transactions,
    })

@login_required
def account_create(request):
    if request.method == 'POST':
        form = AccountRequestForm(request.POST)
        if form.is_valid():
            account_request = form.save(commit=False)
            account_request.customer = request.user
            account_request.save()
            messages.success(request, 'Your account request has been submitted for approval.')
            return redirect('accounts:account_list')
    else:
        form = AccountRequestForm()
    
    return render(request, 'accounts/account_create.html', {'form': form})