from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=200,primary_key=True)
class web_page(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
class a_r(models.Model):
    name=models.ForeignKey(web_page,on_delete=models.CASCADE)
    date=models.DateField()