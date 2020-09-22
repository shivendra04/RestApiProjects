from django.shortcuts import render
from testApp.models import Author,Book
from testApp.serializers import AuthorSerialser,BookSerialser
from rest_framework import generics

class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerialser

class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerialser


class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerialser

class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerialser
