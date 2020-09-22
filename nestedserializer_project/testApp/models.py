from django.db import models

# Create your models here.
class Author(models.Model):
    last_name=models.CharField(max_length=256)
    first_name=models.CharField(max_length=256)
    subject=models.CharField(max_length=256)
    def __str__(self):
        return self.first_name
class Book(models.Model):
    title=models.CharField(max_length=256)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book_by_author')
    release_date=models.DateField()
    rating=models.IntegerField()
    def __str__(self):
        return self.title
