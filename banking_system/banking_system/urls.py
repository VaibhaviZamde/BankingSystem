"""
URL configuration for banking_system project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core import views as core_views
from accounts import views
from django.urls import include, path

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('accounts/login/', 
        auth_views.LoginView.as_view(template_name='core/login.html'), 
        name='login'),
    path('accounts/logout/', 
        auth_views.LogoutView.as_view(), 
        name='logout'),
    path('accounts/register/', 
        core_views.register, 
        name='register'),
    
    path('create/', views.account_create, name='account_create'),
    
    path('banking/', include('accounts.urls')),
    
    
    path('accounts/password_change/', 
         auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), 
         name='password_change'),
    path('accounts/password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
         name='password_change_done'),

    # App-specific URLs
    path('banking/', include('accounts.urls')),
    path('transactions/', include('transactions.urls')),
    path('loans/', include('loans.urls')),
    
    # Dashboard URLs
    path('dashboard/', include('dashboard.urls')),
    
    # Root URL redirects to dashboard
    path('', include('dashboard.urls')),
]

# Static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)