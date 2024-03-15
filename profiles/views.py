from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile_view(request):
    #Fetch or create UserProfile
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    
    #Debugging Print Statements
    print("Profile created:", created)
    
    if request.method == 'POST':
        #Debugging Print Statements
        print("Form data:", request.POST)
        print("Files:", request.FILES)

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profiles:profile_view')
    else:
        form = UserProfileForm(instance=user_profile)

    # Pass form to the template context
    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})
