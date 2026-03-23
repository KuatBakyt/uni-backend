from django.contrib import admin
from .models import Course, Enrollment, Grade

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "program", "teacher", "credits")
    list_filter = ("program", "teacher")
    search_fields = ("name",)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "status")
    list_filter = ("status", "course")
    search_fields = ("student__name", "course__name")

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("enrollment", "value", "date")
    list_filter = ("date",)
    search_fields = ("enrollment__student__name", "enrollment__course__name")