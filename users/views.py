from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from .models import UserProfile, Order, Wishlist  # Assuming you have a Wishlist model

@login_required
def user_profile(request):
    """View for users to view and update their own profile and order history."""
    user = request.user
    user_profile, _ = UserProfile.objects.get_or_create(user=user)
    
    # Handle profile update
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')  # Updated redirect to the profile name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user_profile)

    # Fetch the user's order history
    orders = Order.objects.filter(user=user).order_by('-order_date')

    # Fetch the user's wishlist items
    wishlist = Wishlist.objects.filter(user=user)  # Adjust based on your actual Wishlist model

    # Handle account deletion
    if request.method == 'POST' and 'delete_account' in request.POST:
        user_profile.delete()
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'orders': orders,
        'wishlist': wishlist,
    })

@login_required
def delete_account(request):
    """View to delete the user's account."""
    if request.method == 'POST':
        user = request.user
        UserProfile.objects.filter(user=user).delete()
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')
    return render(request, 'confirm_delete.html')
