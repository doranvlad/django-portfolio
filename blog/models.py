from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
