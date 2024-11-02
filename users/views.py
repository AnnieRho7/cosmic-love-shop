from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, AddressForm  # Import AddressForm
from .models import UserProfile, Order, Wishlist, Address  # Import Address model

@login_required
def user_profile(request):
    """View for users to view and update their own profile and order history."""
    user = request.user
    user_profile, _ = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user_profile)

    # Fetch user's orders, wishlist, and addresses
    orders = Order.objects.filter(user=user).order_by('-date')
    wishlist = Wishlist.objects.filter(user=user)
    addresses = Address.objects.filter(user=user)  # Fetch user's addresses

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'orders': orders,
        'wishlist': wishlist,
        'addresses': addresses,  # Pass user's addresses to template
    })

@login_required
def manage_addresses(request):
    addresses = Address.objects.filter(user=request.user)

    # Check if we are editing an address
    editing_address_id = request.session.get('editing_address_id')
    address_form = AddressForm(request.POST or None, instance=Address.objects.get(id=editing_address_id) if editing_address_id else None)

    if request.method == "POST":
        # Adding a new address
        if "add_address" in request.POST and address_form.is_valid():
            address_form.instance.user = request.user
            address_form.save()
            messages.success(request, "Address added successfully.")
            return redirect("manage_addresses")

        # Editing an address: Load address into session for editing
        elif "edit_address" in request.POST:
            address_id = request.POST.get("address_id")
            request.session['editing_address_id'] = address_id
            return redirect("manage_addresses")

        # Updating an existing address
        elif "update_address" in request.POST and address_form.is_valid():
            address_form.save()
            del request.session['editing_address_id']  # Clear session after update
            messages.success(request, "Address updated successfully.")
            return redirect("manage_addresses")

        # Deleting an address
        elif "delete_address" in request.POST:
            address_id = request.POST.get("address_id")
            address = get_object_or_404(Address, id=address_id, user=request.user)
            address.delete()
            messages.success(request, "Address deleted successfully.")
            return redirect("manage_addresses")

        # Cancel editing an address
        elif "cancel_edit" in request.POST:
            if 'editing_address_id' in request.session:
                del request.session['editing_address_id']  # Clear the session to cancel editing
            return redirect("manage_addresses")

    return render(request, 'addresses.html', {
        'address_form': address_form,
        'addresses': addresses,
        'editing_address_id': editing_address_id,
    })
    
    
@login_required
def delete_account(request):
    """View to delete the user's account directly from the profile."""
    if request.method == 'POST':
        user = request.user
        UserProfile.objects.filter(user=user).delete()
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')
    return HttpResponseForbidden()  # This shouldn't be called directly
