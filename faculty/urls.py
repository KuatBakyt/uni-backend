from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, ProgramViewSet, TeacherViewSet, EventViewSet, DocumentViewSet

router = DefaultRouter()
router.register(r'faculty', FacultyViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'events', EventViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]