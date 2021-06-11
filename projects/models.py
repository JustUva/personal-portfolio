from django.db import models
import os

# Create your models here.
class Project(models.Model):

    path = "/home/uva/Projects/portfolio/projects/static/img"
    #os.path.relpath(path, os.curdir)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    # image = models.ImageField()
    image = models.FilePathField(path=os.path.relpath(path, os.curdir)) # this line gives me trouble when trying to see this table from django admin, when removed everything works fine

    def __str__(self):
        return self.title
