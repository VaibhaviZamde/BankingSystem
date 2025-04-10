from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as core_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('accounts/register/', core_views.register, name='register'),
]