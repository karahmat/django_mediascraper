from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Headline(models.Model):
  title = models.CharField(max_length=200)
  media_name = models.TextField(blank=True)
  date = models.DateField(null=True)
  image = models.URLField(null=True, blank=True)
  link = models.TextField()
  bodytext = models.TextField(blank=True)  
  requestor = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

class Search(models.Model):
    search_indonesian = models.TextField(max_length=20)
    search_english = models.TextField(max_length=20)