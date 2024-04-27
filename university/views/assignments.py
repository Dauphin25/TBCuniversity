from django.shortcuts import render, redirect
from university.models.assignment import Assignment
from university.forms import AssignmentForm
from django.contrib.auth.decorators import login_required
from university.models.Taking_Subjects import TakingSubjects


@login_required
def create_assignment(request):
    professor = request.user.professor

    if request.method == 'POST':
        form = AssignmentForm(request.POST, professor=professor)
        if form.is_valid():
            form.save()
            return redirect('assignments')
    else:
        form = AssignmentForm(professor=professor)
    return render(request, 'university/create_assignment.html', {'form': form})


@login_required
def assignments(request):
    if hasattr(request.user, 'student'):
        student = request.user.student

        # Get the courses the student is enrolled in
        enrolled_courses = TakingSubjects.objects.filter(student=student).values_list('course', flat=True)

        # Filter assignments based on the enrolled courses
        assignments = Assignment.objects.filter(course__in=enrolled_courses)

        return render(request, 'university/assignment.html', {'assignments': assignments})
    else:
        # Handle the case when the user is not a student
        # Redirect to another page or display an error message
        return redirect('university:dashboard')  # Redirect to dashboard or another suitable page