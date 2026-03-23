from django.contrib import admin
from .models import Faculty, Program, Teacher, Event, Document

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "head")
    search_fields = ("name", "head")

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "faculty", "duration")
    list_filter = ("faculty",)
    search_fields = ("name",)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "faculty", "research_area")
    list_filter = ("faculty", "title")
    search_fields = ("name", "research_area")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "faculty")
    list_filter = ("faculty", "date")
    search_fields = ("title",)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "faculty", "file_url")
    list_filter = ("faculty",)
    search_fields = ("title",)