from django.shortcuts import render, redirect
from .form import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

            return redirect('login')
    form = UserRegistrationForm()
    return render(request,'users/register.html', {'form' : form})


@login_required
def profile(request):
    return render(request,'users/profile.html')

