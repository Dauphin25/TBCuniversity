from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from university.forms import LoginForm

from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if hasattr(user, 'student'):
                    user_type = 'student'
                    name = f'{user.student.first_name} {user.student.last_name}'
                elif hasattr(user, 'professor'):
                    user_type = 'professor'
                    name = f'{user.professor.first_name} {user.professor.last_name}'
                else:
                    # Handle the case when the user is neither a student nor a professor
                    user_type = 'user'
                    name = user.username

                messages.success(request, f'Hello {name}, you have successfully logged in as a {user_type}.')
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'university/login.html', {'form': form})