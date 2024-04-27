from django.shortcuts import render
from django.contrib import messages


def home(request):
    return render(request, 'university/home.html', {'messages': messages.get_messages(request)})
