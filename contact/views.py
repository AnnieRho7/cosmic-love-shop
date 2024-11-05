from django.shortcuts import render, redirect
from .forms import CollaborateForm

def contact_view(request):
    if request.method == 'POST':
        form = CollaborateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = CollaborateForm()

    return render(request, 'contact/contact.html', {'form': form})
