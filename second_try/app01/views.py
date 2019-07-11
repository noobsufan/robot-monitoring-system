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
    print(group_list)
    for row in group_list:
        print(row.id,row.title)



    return HttpResponse('database control successfully!')