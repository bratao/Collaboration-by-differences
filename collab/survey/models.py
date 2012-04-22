from django.db import models

class Survey(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    survey = models.ForeignKey(Survey)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()