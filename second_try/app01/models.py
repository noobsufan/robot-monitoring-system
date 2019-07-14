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
        

class User(models.Model):
    '''管理员信息'''
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    admin = models.IntegerField(default=0)
    pwd = models.CharField(max_length=64)

'''多对多例子'''
class Boy(models.Model):
    name = models.CharField(max_length=32)
    # m = models.ManyToManyField('Girl')

class Girl(models.Model):
    nick = models.CharField(max_length=32)
    # m = models.ManyToManyField('Boy')


'''第三张表,存Boy和Gril的关系,但是可以省略,Django自己帮忙生成了,只需要:
    m = models.ManyToManyField('Girl')    m = models.ManyToManyField('Boy')
    但是只能3列！！！
'''
class Love(models.Model):
    b = models.ForeignKey('Boy',on_delete=models.CASCADE)
    g = models.ForeignKey('Girl',on_delete=models.CASCADE)

    # 添加联合索引
    class Meta:
        unique_together=[
            ('b','g'),
        ]

# Django自己生成的第三张表,没有办法直接用类进行操作,间接操作

