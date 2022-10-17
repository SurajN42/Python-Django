from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    age = models.IntegerField()

    def __str__(self):
        return self.name 

class Books(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE) 
    name = models.CharField(max_length=50)
    cost = models.IntegerField() 

    def __str__(self):
        return self.name
