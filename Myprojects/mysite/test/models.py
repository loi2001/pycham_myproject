from django.db import models

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    date_time = models.DateTimeField()

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=  100)
    void = models.IntegerField(default=0)