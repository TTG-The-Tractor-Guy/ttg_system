from django.urls import path, include
from . import views

urlpatterns = [
    path('status/', views.status_view, name='status_view'),
]
