from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutor
from rest_framework.response import Response
from rest_framework import status
from tutor.serializers import TutorSerializer
from rest_framework.views import APIView

def say_hello(request):
    return HttpResponse('Hello world!!! This is the login endpoint.')

# GET list of tutors
class TutorList(APIView):
    def get(self, request):
        movies = Tutor.objects.all() # get list of all Movies from DB
        serializer = TutorSerializer(movies, many=True) # convert raw output to JSON structure
        return Response(serializer.data, status=status.HTTP_200_OK) # return JSON response

# POST new tutor
class TutorCreate(APIView):
    def post(self, request):
        serializer = TutorSerializer(data=request.data) # converts request to JSON response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # returns JSON response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# run command "python3 manage.py makemigrations" to execute this sql query
# query to add tutor
# name = input("name:")
# email = input("email:")
# password = input("password:")
# test = Tutor(full_name=name, email=email, password=password)
# test.save()

# RAW SQL COMMAND EXAMPLE (SELECT)
for p in Tutor.objects.raw("SELECT * FROM tutor"):
    print("tutor::",p.full_name,p.email)

#UPDATE COMMAND EXAMPLE'
query = 'update tutor set full_name="adith" WHERE full_name="adit";'
Tutor.objects.raw(query)

for p in Tutor.objects.raw("SELECT * FROM tutor"):
    print("tutor::",p.full_name,p.email)
