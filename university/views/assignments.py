from django.shortcuts import render, redirect
from university.models.assignment import Assignment
from university.forms import AssignmentForm, AssignmentSubmissionForm
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

        # Filter available assignments based on the enrolled courses
        assignments = Assignment.objects.filter(course__in=enrolled_courses, is_completed=False)

        # Filter completed assignments based on the enrolled courses
        completed_assignments = Assignment.objects.filter(course__in=enrolled_courses, is_completed=True)

        if request.method == 'POST':
            form = AssignmentSubmissionForm(request.POST, request.FILES)
            if form.is_valid():
                assignment_id = form.cleaned_data['assignment_id']
                submission_file = form.cleaned_data['submission']

                # Save the submission to the database and mark the assignment as completed
                assignment = Assignment.objects.get(id=assignment_id)
                assignment.submission = submission_file
                assignment.is_completed = True
                assignment.save()

                # Redirect to prevent form resubmission
                return redirect('assignments')
        else:
            form = AssignmentSubmissionForm()

        return render(request, 'university/assignment.html', {'assignments': assignments, 'completed_assignments': completed_assignments, 'form': form})
    else:
        return redirect('home')