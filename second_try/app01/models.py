from django.db import models

# Create your models here.

class UserInfo(models.Model):
    '''员工'''
    nid = models.AutoField(primary_key=True)   # 自增的主键，可以不写，自动也会生成
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(null=True)                    # 新增字段，null=true表示之前有的数据该列可以为null
                                                                                            # 或者 default=1 
    # ug_id
    ug = models.ForeignKey("UserGroup",null = True,on_delete=models.CASCADE)

class UserGroup(models.Model):
    """部门"""
    title = models.CharField(max_length = 32)
        