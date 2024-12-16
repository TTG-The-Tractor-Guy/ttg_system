from django.urls import path, include
from . import views

urlpatterns = [
    path('status/', views.status_view, name='status_view'),
    # path('api/auth/', include('dj_rest_auth.urls')),
    # path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    
    # # Social Authentication URLs (For Google, Facebook, etc.)
    # path('api/social-auth/', include('allauth.socialaccount.urls')),
    path('auth/', include('dj_rest_auth.urls')),  # Basic authentication endpoints
    # path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
