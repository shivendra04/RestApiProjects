from testApp.models import Author,Book
from rest_framework import serializers

class BookSerialser(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class AuthorSerialser(serializers.ModelSerializer):
    book_by_author=BookSerialser(read_only=True,many=True)# nesting serializer
    class Meta:
        model=Author
        fields='__all__'
