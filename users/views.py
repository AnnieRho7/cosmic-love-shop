from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponseForbidden
from .forms import UserForm, ProfileForm, AddressForm, NewsletterSubscriptionForm
from .models import UserProfile, Order, Wishlist, Address
from .mailchimp import MailchimpService

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
    addresses = Address.objects.filter(user=user)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'orders': orders,
        'wishlist': wishlist,
        'addresses': addresses,
    })

@login_required
def manage_addresses(request):
    addresses = Address.objects.filter(user=request.user)

    # Retrieve address instance if in edit mode
    editing_address_id = request.session.get('editing_address_id')
    address_instance = None
    if editing_address_id:
        try:
            address_instance = Address.objects.get(id=editing_address_id, user=request.user)
        except Address.DoesNotExist:
            del request.session['editing_address_id']

    address_form = AddressForm(request.POST or None, instance=address_instance)

    if request.method == "POST":
        if "add_address" in request.POST and address_form.is_valid():
            address_form.instance.user = request.user
            address_form.save()
            messages.success(request, "Address added successfully.")
            return redirect("manage_addresses")

        elif "update_address" in request.POST and address_form.is_valid():
            address_form.save()
            messages.success(request, "Address updated successfully.")
            del request.session['editing_address_id']
            return redirect("manage_addresses")

        elif "edit_address" in request.POST:
            address_id = request.POST.get("address_id")
            request.session['editing_address_id'] = address_id
            return redirect("manage_addresses")

        elif "delete_address" in request.POST:
            address_id = request.POST.get("address_id")
            address = get_object_or_404(Address, id=address_id, user=request.user)
            address.delete()
            messages.success(request, "Address deleted successfully.")
            if 'editing_address_id' in request.session and request.session['editing_address_id'] == address_id:
                del request.session['editing_address_id']
            return redirect("manage_addresses")

        elif request.GET.get('cancel'):
            if 'editing_address_id' in request.session:
                del request.session['editing_address_id']
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
    return HttpResponseForbidden()

@require_http_methods(["POST"])
def newsletter_signup(request):
    """Handle newsletter subscriptions"""
    form = NewsletterSubscriptionForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        mailchimp = MailchimpService()
        
        # Add subscriber to Mailchimp
        merge_fields = {}
        if request.user.is_authenticated:
            merge_fields.update({
                "FNAME": request.user.first_name,
                "LNAME": request.user.last_name,
            })
        
        success = mailchimp.add_subscriber(
            email=email,
            merge_fields=merge_fields
        )
        
        if success:
            messages.success(
                request, 
                "Thank you for subscribing! Please check your email to confirm your subscription."
            )
        else:
            messages.error(
                request,
                "There was an error with your subscription. Please try again later."
            )
        
        # Return JSON response for AJAX requests
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'success' if success else 'error',
                'message': str(messages.get_messages(request)[-1])
            })
    else:
        messages.error(request, "Please provide a valid email address.")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'error',
                'message': "Please provide a valid email address."
            })
    
    # Redirect to the previous page for non-AJAX requests
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def toggle_newsletter_subscription(request):
    """Toggle newsletter subscription status for logged-in users"""
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to manage your newsletter subscription.")
        return redirect('login')
    
    try:
        mailchimp = MailchimpService()
        user_profile = UserProfile.objects.get(user=request.user)
        
        # Toggle subscription status
        new_status = "subscribed" if not user_profile.newsletter_subscribed else "unsubscribed"
        
        success = mailchimp.update_subscriber(
            email=request.user.email,
            merge_fields={
                "FNAME": request.user.first_name,
                "LNAME": request.user.last_name,
                "STATUS": new_status
            }
        )
        
        if success:
            user_profile.newsletter_subscribed = not user_profile.newsletter_subscribed
            user_profile.save()
            status_message = "subscribed to" if user_profile.newsletter_subscribed else "unsubscribed from"
            messages.success(request, f"You have successfully {status_message} our newsletter.")
        else:
            messages.error(request, "There was an error updating your subscription. Please try again later.")
            
    except UserProfile.DoesNotExist:
        messages.error(request, "User profile not found.")
    
    return redirect('profile')