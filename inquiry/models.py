import datetime

from django.db import models


# Create your models here.
class writing(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    writer = models.CharField(max_length=30)
    comm_content = models.TextField(default="NotExistComments")
    comm_pub_date = models.DateTimeField('comment date published', default=datetime.datetime.now())
