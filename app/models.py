from django.db import models
from django.core import validators
from django import forms

# Create your models here.
def check_for_a(x):
    if x[0].lower() == 'a':
        raise forms.ValidationError('poraa poo***')
class Topic(models.Model):
    topic_name = models.CharField(max_length=100,primary_key=True,validators=[check_for_a,])
    def __str__(self):
        return self.topic_name
class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,validators=[validators.MinLengthValidator(5)])
    url = models.URLField()
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    data = models.DateField()
    author = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.author