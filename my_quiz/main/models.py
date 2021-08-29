from django.db import models


class Question(models.Model):
    choices = [('True', 'True'), ('False', 'False')]
    text = models.CharField('Вопрос', max_length=250)
    answr = models.CharField('Ответ', max_length=5, choices=choices, default='Unspecified')

    def __str__(self):
        return self.text

