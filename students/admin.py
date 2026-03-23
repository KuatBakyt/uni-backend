from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "program", "enrollment_date")
    list_filter = ("program", "enrollment_date")
    search_fields = ("name", "email")