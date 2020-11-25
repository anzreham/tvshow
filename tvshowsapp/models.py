from django.db import models
from datetime import datetime, date
from django import forms

class DateInput (forms.DateInput):
    input_type = 'date'

class Show  (models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    relasDate = models.DateField()
    desc = models.CharField(max_length=255) 


