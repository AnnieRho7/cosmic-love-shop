from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponseForbidden
from django.conf import settings
from .forms import UserForm, ProfileForm, AddressForm, NewsletterSubscriptionForm
from .models import UserProfile, Order, Wishlist, Address, NewsletterSubscriber, Product
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
        subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
        
        try:
            mailchimp = MailchimpService()
            
            member_info = {
                "email_address": email,
                "status": "subscribed",
                "merge_fields": {}
            }
            
            if request.user.is_authenticated:
                member_info["merge_fields"].update({
                    "FNAME": request.user.first_name,
                    "LNAME": request.user.last_name,
                })
            

            mailchimp.client.lists.add_list_member(
                settings.MAILCHIMP_AUDIENCE_ID,
                member_info
            )
            messages.success(request, "Thank you for subscribing to our newsletter!")
            
        except Exception as e:
            if 'already a list member' in str(e).lower():
                messages.success(request, "You're already subscribed to our newsletter!")
            else:
                messages.success(request, "Thank you for subscribing!")
    else:
        messages.error(request, "Please provide a valid email address.")

    return redirect(request.META.get('HTTP_REFERER', 'home'))


def toggle_newsletter_subscription(request):
    """Toggle newsletter subscription status for logged-in users"""
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to manage your newsletter subscription.")
        return redirect('login')
    
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        email = request.user.email
        
        try:
            mailchimp = MailchimpService()
            
            if user_profile.newsletter_subscribed:

                try:
                    subscriber = NewsletterSubscriber.objects.get(email=email)
                    subscriber.delete()
                except NewsletterSubscriber.DoesNotExist:
                    pass

                member_info = {
                    "email_address": email,
                    "status": "unsubscribed",
                    "merge_fields": {
                        "FNAME": request.user.first_name,
                        "LNAME": request.user.last_name,
                    }
                }
            else:
                NewsletterSubscriber.objects.get_or_create(email=email)
                member_info = {
                    "email_address": email,
                    "status": "subscribed",
                    "merge_fields": {
                        "FNAME": request.user.first_name,
                        "LNAME": request.user.last_name,
                    }
                }
            
            try:
                mailchimp.client.lists.add_list_member(
                    settings.MAILCHIMP_AUDIENCE_ID,
                    member_info
                )
            except Exception as e:
                if 'already a list member' in str(e).lower():
                    subscriber_hash = mailchimp._get_subscriber_hash(email)
                    mailchimp.client.lists.update_list_member(
                        settings.MAILCHIMP_AUDIENCE_ID,
                        subscriber_hash,
                        member_info
                    )
            
            user_profile.newsletter_subscribed = not user_profile.newsletter_subscribed
            user_profile.save()
            
            status_message = "subscribed to" if user_profile.newsletter_subscribed else "unsubscribed from"
            messages.success(request, f"You have successfully {status_message} our newsletter.")
            
        except Exception as e:
            messages.warning(request, "Your subscription preference was updated locally, but there was an issue with the email service.")
            
    except UserProfile.DoesNotExist:
        messages.error(request, "User profile not found.")
    
    return redirect('profile')


@login_required
def add_to_wishlist(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        wishlist_item = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).first()
        
        if wishlist_item:
            wishlist_item.delete()
            status = 'removed'
            message = 'Product removed from wishlist'
            is_in_wishlist = False
        else:

            Wishlist.objects.create(
                user=request.user,
                product=product
            )
            status = 'added'
            message = 'Product added to wishlist'
            is_in_wishlist = True
        
        updated_wishlist = Wishlist.objects.filter(user=request.user).select_related('product')
        
        wishlist_items = [{
            'id': item.id,
            'product_id': item.product.id,
            'product_name': item.product.name,
        } for item in updated_wishlist]
        
        return JsonResponse({
            'status': status,
            'message': message,
            'in_wishlist': is_in_wishlist,
            'wishlist': wishlist_items,
            'product_id': product_id
        })
        
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(Wishlist, id=item_id, user=request.user)
    product_id = wishlist_item.product.id
    wishlist_item.delete()
    messages.success(request, 'Item removed from wishlist')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'removed',
            'message': 'Product removed from wishlist',
            'in_wishlist': False
        })
    return redirect('profile')


@login_required
def check_wishlist_status(request, product_id):
    """Check if a product is in user's wishlist"""
    try:
        is_in_wishlist = Wishlist.objects.filter(
            user=request.user,
            product_id=product_id
        ).exists()
        
        return JsonResponse({
            'in_wishlist': is_in_wishlist,
            'product_id': product_id
        })
    except Exception as e:
        return JsonResponse({
            'error': str(e),
            'in_wishlist': False
        }, status=400)


@login_required
def get_wishlist(request):
    """Get all wishlist items for the current user"""
    try:
        wishlist_items = Wishlist.objects.filter(user=request.user)
        items = [{
            'id': item.id,
            'product_id': item.product.id,
            'product_name': item.product.name,
            'in_wishlist': True
        } for item in wishlist_items]
        
        return JsonResponse({
            'wishlist': items
        })
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=400)