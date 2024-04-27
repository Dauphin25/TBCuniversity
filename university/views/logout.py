from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')
