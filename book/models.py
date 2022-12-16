from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="media/")
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now_add=True)


