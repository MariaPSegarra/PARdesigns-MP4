from django.shortcuts import render
from .models import Category

# Create your views here.


def all_services(request):
    """ A view to show all services """

    services = Category.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


