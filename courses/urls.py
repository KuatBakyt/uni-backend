from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, EnrollmentViewSet, GradeViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]