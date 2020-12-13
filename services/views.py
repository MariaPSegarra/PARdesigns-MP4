from django.shortcuts import (
    render, redirect,
    reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Category, Design
from .forms import CategoryForm

# Create your views here.


def all_services(request):
    """ A view to show all services """

    services = Category.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('services'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            services = categories.filter(queries)

    context = {
        'services': services,
        'search_term': query,

    }

    return render(request, 'services/services.html', context)


def service_page(request, category_id):
    """ A view to show each service page with their designs """

    services = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)
    designs = Design.objects.all()

    context = {
        'services': services,
        'category': category,
        'designs': designs,
    }

    return render(request, 'services/service_page.html', context)


@login_required
def add_service(request):
    """ Add a service to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Service added successfully!')
            return redirect(reverse('service_page', args=[category.id]))
        else:
            messages.error(
                request, 'Failed to add new service. Please try again.')
    else:
        form = CategoryForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_service(request, category_id):
    """ Edit a service in the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated category!')
            return redirect(reverse('service_page', args=[category.id]))
        else:
            messages.error(
                request, 'Failed to update service. Please try again.')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.name}')

    template = 'services/edit_service.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@login_required
def delete_service(request, category_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Service deleted!')
    return redirect(reverse('services'))
