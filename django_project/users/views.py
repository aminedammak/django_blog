from django.shortcuts import render, redirect
from django.contrib import messages
from .Form import RegisterFormUser


def register(request):
    if request.method == 'POST':
        form = RegisterFormUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('blog-home')
    else:
        form = RegisterFormUser()
    return render(request, "users/registerForm.html", {'form': form})