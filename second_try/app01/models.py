from django.db import models

# Create your models here.

class UserInfo(models.Model):
    nid = models.BigAutoField(primary_key=True)   # 自增的主键，可以不写，自动也会生成
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
