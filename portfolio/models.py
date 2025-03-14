from django.db import models

# Create your models here.
#TODO Create a model for the projects

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


#TODO Create a model for the tech stack

class Technologies(models.Model):
    name = models.CharField(max_length=100)
    level = models.TextField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
