from django.db import models


class Todo(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=200)
    isDone=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

class List(models.Model):
    Нэр = models.CharField(max_length=50)
    Тайлбар = models.CharField(max_length=200)
    Огноо = models.DateTimeField(auto_now_add=True)
    Хаяг = models.CharField(max_length=200)
    Мөнгө = models.CharField(max_length=50)


    def __str__(self):
        return self.Нэр[:20]
