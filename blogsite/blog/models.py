from django.db import models
import random
import string
from django.utils.crypto import get_random_string


def random_id():
   rand_str = get_random_string(7)
   return rand_str

# Create your models here.
class Post(models.Model):
    id=models.CharField(primary_key=True,max_length=10,editable=True,default=random_id)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, unique=True)
    blog = models.CharField(max_length=1000)
    date_posted = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

