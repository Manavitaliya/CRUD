from django.contrib import admin
from .models import Student

# Register Student model to appear in Django admin
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'study', 'city', 'mobile', 'percentage')
    search_fields = ('name', 'study', 'city')