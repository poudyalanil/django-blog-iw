from django.db import models
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
class Blog(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True,null=True)
    content = models.TextField()
    author  = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
