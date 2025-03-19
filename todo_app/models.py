from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_of_start = models.DateField()
    date_of_end = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title