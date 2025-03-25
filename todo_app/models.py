from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_of_start = models.DateField()
    date_of_end = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    