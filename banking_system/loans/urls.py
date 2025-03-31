from django.urls import path
from . import views

app_name = 'loans'

urlpatterns = [
    path('', views.loan_list, name='loan_list'),
    path('<int:loan_id>/', views.loan_detail, name='loan_detail'),
    path('create/', views.loan_create, name='loan_create'),
]