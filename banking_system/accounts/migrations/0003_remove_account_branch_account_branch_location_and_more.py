# Generated by Django 5.1.6 on 2025-03-26 04:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='branch',
        ),
        migrations.AddField(
            model_name='account',
            name='branch_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='branch_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('S', 'Savings'), ('C', 'Checking'), ('F', 'Fixed Deposit')], max_length=1),
        ),
        migrations.AlterField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountrequest',
            name='account_type',
            field=models.CharField(choices=[('S', 'Savings'), ('C', 'Checking'), ('F', 'Fixed Deposit')], max_length=1),
        ),
        migrations.AlterField(
            model_name='accountrequest',
            name='processed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='processed_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountrequest',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
    ]
