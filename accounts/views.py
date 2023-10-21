from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    user_profile = request.user
    return render(request, 'profile_view.html', {'user_profile': user_profile})

@login_required
def profile_edit(request):
    user_profile = request.user
    return render(request, 'profile_edit.html', {'user_profile': user_profile})
