from django.shortcuts import render
from rest_framework import viewsets
from .models import Notes
from .serializers import NoteSerializer

from django.http import HttpResponse, JsonResponse  
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# class NotesView(viewsets.ModelViewSet):
#     queryset = Notes.objects.all()
#     serializer_classs = NoteSerializer

class NotesView(APIView):
    def get(self,request):
        notes = Notes.objects.all()
        serialize = NoteSerializer(notes, many=True)
        return Response(serialize.data)
    
    def post(self,request):
        serialize = NoteSerializer(data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)