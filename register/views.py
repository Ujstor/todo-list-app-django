from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('/')
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})
