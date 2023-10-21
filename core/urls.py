from django.urls import path
from .views import portfolio, contact

urlpatterns = [
    path('', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
]