from django.db import models
from django.contrib.auth.models import User
# MinValueValidator　：　登録すつデータに最小値の制限をつける　
from django.core.validators import MinValueValidator

class Board(models.Model):
    title = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if not self.title:
            tmp = 'empty'
        else:
            tmp = self.title
        return str(self.id) + '_' + tmp


class List(models.Model):
    title = models.CharField(max_length=50 ,null=True)
    boardId = models.ForeignKey(Board, on_delete=models.CASCADE)
    index = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if not self.title:
            tmp = 'empty'
        else:
            tmp = self.title
        return str(self.id) + '_' + tmp


class Card(models.Model):
    listId = models.ForeignKey(List, on_delete=models.CASCADE)
    index = models.IntegerField(validators=[MinValueValidator(0)])
    text = models.CharField(max_length=50, null=True)
    boardId = models.ForeignKey(Board, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if not self.text:
            tmp = 'empty'
        else:
            tmp = self.text
        return str(self.id) + '_' + tmp

