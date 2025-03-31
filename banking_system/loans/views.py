from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Loan, LoanPayment
from .forms import LoanApplicationForm
from core.models import Branch

@login_required
def loan_list(request):
    if request.user.is_customer:
        loans = Loan.objects.filter(customer=request.user)
    else:
        loans = Loan.objects.all()
    return render(request, 'loans/loan_list.html', {'loans': loans})

@login_required
def loan_detail(request, loan_id):
    loan = get_object_or_404(Loan, loan_id=loan_id)
    if request.user.is_customer and loan.customer != request.user:
        messages.error(request, "You don't have permission to view this loan.")
        return redirect('loans:loan_list')
    
    payments = loan.payments.all().order_by('-payment_date')
    return render(request, 'loans/loan_detail.html', {
        'loan': loan,
        'payments': payments,
    })

@login_required
def loan_create(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.customer = request.user
            loan.save()
            messages.success(request, 'Your loan application has been submitted for approval.')
            return redirect('loans:loan_list')
    else:
        form = LoanApplicationForm()
    
    return render(request, 'loans/loan_create.html', {'form': form})