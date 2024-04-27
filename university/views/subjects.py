from django.shortcuts import render
from university.models import Course
from university.forms import TakingSubjectsForm
from django.shortcuts import redirect
from university.models.Taking_Subjects import TakingSubjects
from django.contrib.auth.decorators import login_required


@login_required
def my_subjects(request):
    # Get the logged-in student
    student = request.user.student

    # Get the TakingSubjects instances for this student
    my_subjects = TakingSubjects.objects.filter(student=student)

    # Render a template that displays these subjects
    return render(request, 'university/my_subjects.html', {'my_subjects': my_subjects, 'student': student})

def subjects(request):
    courses = Course.objects.all()  # Retrieve all courses from the database
    return render(request, 'university/subjects.html', {'courses': courses})


def taking_subjects(request):
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = TakingSubjectsForm(request.POST)
        if form.is_valid():
            # Check if the student has already reached the maximum number of subjects
            student = form.cleaned_data['student']
            if student.taken_subjects.count() >= 6:
                # If the student already has 6 subjects, return an error message
                error_message = "Each student can take a maximum of 6 subjects."
                return render(request, 'university/taking_subjects.html', {'form': form, 'error_message': error_message})

            # Save the form data if the student can take more subjects
            form.save()
            # Redirect to the same page to display updated data
            return redirect('taking_subjects')
    else:
        # If the request method is not POST, render the form
        form = TakingSubjectsForm()

    # Get all taking subjects grouped by student
    taking_subjects_grouped = {}
    for taking_subject in TakingSubjects.objects.all().order_by('student'):
        student = taking_subject.student
        if student not in taking_subjects_grouped:
            taking_subjects_grouped[student] = []
        taking_subjects_grouped[student].append(taking_subject)

    # Render the template with the form and grouped taking subjects data
    return render(request, 'university/taking_subjects.html', {'form': form, 'taking_subjects_grouped': taking_subjects_grouped})
