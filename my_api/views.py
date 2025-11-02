from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class KafedraViewSet(viewsets.ModelViewSet):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-id')
    serializer_class = TeacherSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer