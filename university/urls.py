from django.urls import path
from university.views.home_page import home
from university.views.login import login_view
from university.views.professor import professors, professor_subjects
from university.views.faculties import faculties
from university.views.subjects import subjects
from university.views.subjects import taking_subjects
from university.views.logout import logout_view
from university.views.subjects import my_subjects
from university.views.assignments import create_assignment, assignments


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('professors/', professors, name='professors'),
    path('faculties/', faculties, name='faculties'),
    path('subjects/', subjects, name='subjects'),
    path('taking_subjects/', taking_subjects, name='taking_subjects'),
    path('logout/', logout_view, name='logout'),
    path('my_subjects/', my_subjects, name='my_subjects'),
    path('professor/subjects/', professor_subjects, name='professor_subjects'),
    path('create_assignment/', create_assignment, name='create_assignment'),
    path('assignments/', assignments, name='assignments'),
]
