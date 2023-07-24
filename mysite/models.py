from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    writer = models.CharField(max_length=30, default='Majornity')