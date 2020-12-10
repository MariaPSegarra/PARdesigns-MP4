from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('<category_id>', views.service_page, name='service_page'),
]