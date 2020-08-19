from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login
    form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})
