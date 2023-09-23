from django.db import models
from djangosnippet import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Snippet(models.Model):
    title = models.CharField('タイトル',max_length=255)
    code = models.TextField('コード',blank=True)
    description = models.TextField('説明',blank=True)
    created_by = models.ForeignKey(get_user_model(),verbose_name='投稿者',on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日',auto_now_add=True)
    updated_at = models.DateTimeField('更新日',auto_now=True)
    
    def __str__(self):
        return self.title
