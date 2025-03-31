from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from accounts.models import Account
from .models import Transaction
from .forms import TransactionForm

@login_required
def transaction_list(request):
    if request.user.is_customer:
        accounts = Account.objects.filter(customer=request.user)
        transactions = Transaction.objects.filter(account__in=accounts).order_by('-timestamp')
    else:
        transactions = Transaction.objects.all().order_by('-timestamp')
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

@login_required
def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.user, request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    transaction_obj = form.save(commit=False)
                    account = transaction_obj.account
                    
                    if transaction_obj.transaction_type == 'D':
                        account.balance += transaction_obj.amount
                    elif transaction_obj.transaction_type == 'W':
                        if account.balance < transaction_obj.amount:
                            raise ValueError("Insufficient balance")
                        account.balance -= transaction_obj.amount
                    
                    transaction_obj.balance_after = account.balance
                    account.save()
                    transaction_obj.save()
                    
                    messages.success(request, 'Transaction completed successfully!')
                    return redirect('transactions:transaction_list')
            except ValueError as e:
                messages.error(request, str(e))
            except Exception as e:
                messages.error(request, 'An error occurred during the transaction.')
    else:
        form = TransactionForm(request.user)
    
    return render(request, 'transactions/transaction_create.html', {'form': form})