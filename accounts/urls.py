from django.urls import include, path
from .views import profile

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', profile, name='profile'),
]