from django.db import models

# Create your models here.
class SurveyAnswers(models.Model):
  # Answers to the 5 questions
  destination = models.CharField(max_length = 200)
  trip_length = models.IntegerField()
  group_size = models.IntegerField()
  pace = models.CharField(max_length = 10) #revisit for error handle
  budget = models.IntegerField()