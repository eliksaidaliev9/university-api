from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'faculties', FacultyViewSet)
router.register(r'kafedras', KafedraViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]