from django.shortcuts import (
    render, redirect,
    reverse, get_object_or_404)
from django.contrib import messages
from django.db.models import Q
from .models import Category, Design

# Create your views here.


def all_services(request):
    """ A view to show all services """

    services = Category.objects.all()
    query = None
    category= None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('services'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
        'search_term': query,

    }

    return render(request, 'services/services.html', context)


def service_page(request, category_id):
    """ A view to show each service page with their designs """

    services = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'services': services,
        'category': category,
    }

    return render(request, 'services/service_page.html', context)
