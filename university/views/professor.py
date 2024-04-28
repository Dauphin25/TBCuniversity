from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from university.models import Professor, Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from university.models.attendance import Attendance
from university.models.course import Course
from university.models.Taking_Subjects import TakingSubjects
from django.contrib import messages


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


def mark_attendance_page(request):
    return render(request, 'university/mark_attendance.html', {})


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


@login_required
def mark_attendance(request, subject_id):
    # Retrieve all attendance records for the specified subject
    all_attendance = Attendance.objects.filter(course=subject_id)

    # Get the subject/course
    subject = get_object_or_404(Course, id=subject_id)

    # Get all students taking the course
    students_taking_course = TakingSubjects.objects.filter(course=subject)

    # Combine subject/course with its associated students
    courses_with_students = [{'course': subject, 'students': students_taking_course}]

    if request.method == 'POST':
        # If the request method is POST, attempt to mark attendance
        date = request.POST.get('date')

        # Check if date is provided
        if not date:
            # If date is not provided, display error message
            messages.error(request, "Please enter a date.")
            return render(request, 'university/mark_attendance.html',
                          {'courses_with_students': courses_with_students, 'all_attendance': all_attendance})

        # Check if there's existing attendance for the chosen date
        existing_attendance = Attendance.objects.filter(course=subject_id, date=date).exists()
        if existing_attendance:
            # If there's existing attendance for the chosen date, display error message
            messages.error(request, "Attendance for this date already exists.")
            return render(request, 'university/mark_attendance.html',
                          {'courses_with_students': courses_with_students, 'all_attendance': all_attendance})

        # Loop through each course and its associated students
        for course_with_students in courses_with_students:
            for student in course_with_students['students']:
                # Get attendance status for each student
                attended = request.POST.get(f'attended_{student.student.id}', False)

                # Create attendance record for each student
                Attendance.objects.create(student=student.student, course=course_with_students['course'], date=date,
                                          is_present=attended)

        # Display success message after marking attendance
        messages.success(request, "Attendance marked successfully.")

        # Return the same page with success message displayed
        return render(request, 'university/mark_attendance.html',
                      {'courses_with_students': courses_with_students, 'all_attendance': all_attendance})

    # If the request method is not POST, render the page with attendance data
    return render(request, 'university/mark_attendance.html',
                  {'courses_with_students': courses_with_students, 'all_attendance': all_attendance})
