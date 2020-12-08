from django.contrib import admin
from .models import Design, Category

# Register your models here.


class DesignAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'name',
        'category',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'price',
    )


admin.site.register(Design)
admin.site.register(Category)
