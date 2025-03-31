# Generated by Django 5.1.6 on 2025-03-25 17:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(choices=[('P', 'Personal'), ('H', 'Home'), ('E', 'Education'), ('B', 'Business')], max_length=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration_months', models.IntegerField()),
                ('start_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected'), ('D', 'Disbursed'), ('C', 'Closed')], default='P', max_length=1)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('purpose', models.TextField()),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_loans', to=settings.AUTH_USER_MODEL)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.branch')),
                ('customer', models.ForeignKey(limit_choices_to={'is_customer': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoanPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('principal_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('interest_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('remaining_balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='loans.loan')),
            ],
        ),
    ]
