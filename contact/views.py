from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CollaborateForm

def contact_view(request):
    if request.method == 'POST':
        form = CollaborateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CollaborateForm()

    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)