from django.shortcuts import render

# Create your views here.

from django.shortcuts import  HttpResponse

def index(request):
    user_list = [
        'alex','eric','tony'
    ]

    return render(request,'index.html',{'user_list':user_list})


# def edit(request,a1):
#     print(a1)
#     return HttpResponse('---')
def edit(request,a):
    print(a)
    return HttpResponse('----')

from django.urls import reverse
def index_name(request):
        user_list = [
        'alex','eric','tony'
        ]
        v = reverse('name_index')
        print(v)
        return render(request,'index.html',{'user_list':user_list})


# 数据库相关操作 通过index_db
    # 增删改查
from app01 import models
def index_db(request):
    # 新增
    # models.UserGroup.objects.create(title='销售部')
    # models.UserInfo.objects.create(username='root',password='pwd',age=18,ug_id=1)

    # 查找
    group_list = models.UserGroup.objects.all()
    group_list = models.UserGroup.objects.filter(id=1)
    # 神奇的双划线__
    # group_list = models.UserGroup.objects.filter(id__gt=1)  # 大于
    # group_list = models.UserGroup.objects.filter(id__lt=1)  # 小于
    print(group_list)
    for row in group_list:
        print(row.id,row.title)
    return HttpResponse('database control successfully!')

    # 删除
    # models.UserGroup.objects.filter(id=2).delete()
    # 更新
    # models.UserGroup.objects.filter(id=2).update(title='公关部')


def show_usr_info(request):
    info_list = models.User.objects.all()
    return render(request,'show_usr_info.html',{'info_list':info_list})


'''多对多'''
# from app01 import models
def test(request):
    # objs = [
    #     models.Boy(name='方绍伟'),
    #     models.Boy(name='由秦兵'),
    #     models.Boy(name='陈涛'),
    #     models.Boy(name='闫龙'),
    #     models.Boy(name='吴燕祖'),
    #     ]
    # models.Boy.objects.bulk_create(objs,5)
    #
    # objss = [
    #     models.Girl(nick='小鱼'),
    #     models.Girl(nick='小周'),
    #     models.Girl(nick='小猫'),
    #     models.Girl(nick='小钩'),
    #     ]
    # models.Girl.objects.bulk_create(objss,5)

    # models.Love.objects.create(b_id=1, g_id=1)
    # models.Love.objects.create(b_id=1, g_id=4)
    # models.Love.objects.create(b_id=2, g_id=4)
    # models.Love.objects.create(b_id=2, g_id=2)


    '''1.取出查询和方绍伟有关系的girl(方式1，反向url)'''
    obj = models.Boy.objects.filter(name='方绍伟').first()
    love_list = obj.love_set.all()
    for row in love_list:
        print(row.g.nick)

    # 2. 方式2,__双下划线连表
    love_list = models.Love.objects.filter(b__name='方绍伟')
    for row in love_list:   # 每循环一次,跨表一次
        print(row.g.nick)

    # 3. 改进
    love_list = models.Love.objects.filter(b__name='方绍伟').values('g__nick')  # values 拿到的是字典
    for item in love_list:
        print(item['g__nick'])

    # 4.再改进
    love_list = models.Love.objects.filter(b__name='方绍伟').select_related('g')  # 拿到的是对象
    for obj in love_list:
        print(obj.g.nick)


    # return  render(request,'test.html')
    return HttpResponse('...')