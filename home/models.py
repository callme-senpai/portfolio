from django.db import models

# Create your models here.
class Home(models.Model):
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()