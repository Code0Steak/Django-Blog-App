from django.shortcuts import render, redirect
from .form import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


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

    if request.method == 'POST':
        uForm = UserUpdateForm(request.POST, instance=request.user)
        pForm = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)

        #save updates if both forms are valid
        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            messages.success(request, 'Acount successfully updated!')
            return redirect('profile')

    else:
        uForm = UserUpdateForm(instance=request.user)
        pForm = ProfileUpdateForm()#instance=request.user.profile)
    context = {
        'uForm': uForm,
        'pForm': pForm,
    }
    return render(request,'users/profile.html', context)

