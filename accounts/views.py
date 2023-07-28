from django.contrib.auth import login
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # login(request, user)
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'mysite/accounts/signup.html', {'form': form})
