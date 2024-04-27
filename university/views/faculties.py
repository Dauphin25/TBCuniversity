from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from university.models import Faculty


def faculties(request):
    faculties_list = Faculty.objects.all()  # Retrieve all faculties from the database

    # Number of faculties per page
    per_page = 2

    paginator = Paginator(faculties_list, per_page)

    # Get the current page number from the request
    page_number = request.GET.get('page')

    try:
        # Get the faculties for the requested page
        faculties = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        faculties = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        faculties = paginator.page(paginator.num_pages)

    return render(request, 'university/faculties.html', {'faculties': faculties})
