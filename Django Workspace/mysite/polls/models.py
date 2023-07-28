from django.db import models

# Create your models here.
class testModel(models.Model):
    field = models.CharField(max_length= 200)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    votes = models.IntegerField(default=0,verbose_name="Vote Count")



    
