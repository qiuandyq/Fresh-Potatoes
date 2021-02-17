from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('survey')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')

def survey(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instanct=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Updated')
            return redirect('home')
    else:
        p_form = ProfileUpdateForm(instanct=request.user.profile)

    return render(request, 'users/survey.html', {'p_form': p_form})