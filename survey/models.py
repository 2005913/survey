from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_t=models.CharField(max_length=200)
    q_date=models.DateTimeField('날짜 적힘')

    def __str__(self):
        return self.question_t

    def was_published_recently(self):
        return self.q_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text