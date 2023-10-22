from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

# @login_required
# def profile_view(request):
#     user_profile = request.user
#     return render(request, 'profile_view.html', {'user_profile': user_profile})

@login_required
def profile(request):
    user_profile = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'profile.html', {'form': form})

