from django.shortcuts import render

def privacy_policy(request):
    return render(request, 'legal/privacy_policy.html')

def terms_and_conditions(request):
    return render(request, 'legal/terms_and_conditions.html')

def return_refund_policy(request):
    return render(request, 'legal/return_refund_policy.html')

def cookie_policy(request):
    return render(request, 'legal/cookie_policy.html')