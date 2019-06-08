from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ViewSet):
 
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
 
    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)

 
class StudentGenericViewSet(viewsets.GenericViewSet):
 
   def get_queryset(self):
       queryset = Student.objects.all()
       return queryset
 
   def get_object(self):
       queryset = self.get_queryset()
       obj = queryset.get(pk=self.kwargs['pk'])
       return obj
   
   def list(self, request):
       queryset = self.get_queryset()
       serializer = StudentSerializer(queryset, many=True)
       return Response(serializer.data)
 
   def retrieve(self, request, **kwargs):
       obj = self.get_object()
       serializer = StudentSerializer(obj)
       return Response(serializer.data)


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
