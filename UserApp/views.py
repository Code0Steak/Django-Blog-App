from django.shortcuts import render, redirect
from .form import UserRegistrationForm
from django.contrib import messages

def registerUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            # messages.debug
            # messages.error
            messages.success(request, f'Your account is created, {username}!!')
            # messages.warning
            # messages.info

            return redirect('blog-home')
    form = UserRegistrationForm()
    return render(request,'users/register.html', {'form' : form})

