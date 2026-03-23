from rest_framework import serializers
from .models import Faculty, Program, Teacher, Event, Document

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"