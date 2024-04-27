from django.shortcuts import render
from university.models import Professor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from university.models.course import Course
from university.models.Taking_Subjects import TakingSubjects


@login_required
def professor_subjects(request):
    professor = request.user.professor
    courses = Course.objects.filter(professor=professor)
    courses_with_students = []

    for course in courses:
        students_taking_course = TakingSubjects.objects.filter(course=course)
        courses_with_students.append({'course': course, 'students': students_taking_course})

    return render(request, 'university/professor_subjects.html',
                  {'courses_with_students': courses_with_students})


def professors(request):
    professors_list = Professor.objects.all()  # Retrieve all professors from the database

    # Number of professors per page
    per_page = 4

    paginator = Paginator(professors_list, per_page)

    # Get the current page number from the request
    page_number = request.GET.get('page')

    try:
        # Get the professors for the requested page
        professors = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        professors = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        professors = paginator.page(paginator.num_pages)

    return render(request, 'university/professors.html', {'professors': professors})
