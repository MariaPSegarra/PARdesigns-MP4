from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('<int:category_id>/', views.service_page, name='service_page'),
    path('add/', views.add_service, name='add_service'),
    path('edit/<int:category_id>/', views.edit_service, name='edit_service'),
    path('delete/<int:category_id>/',
         views.delete_service, name='delete_service'),

]
