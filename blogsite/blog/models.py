from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, unique=True)
    blog = models.CharField(max_length=1000)
    date_posted = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

