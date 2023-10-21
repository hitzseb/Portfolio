from django.urls import include, path
from .views import profile_view, profile_edit

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', profile_view, name='profile_view'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]