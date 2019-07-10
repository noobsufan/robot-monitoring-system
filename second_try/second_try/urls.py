"""second_try URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render,redirect    
from database_urls import db, db_call
from django.http import JsonResponse
import time
#   用于计算cookie超时时间
import datetime
from datetime import timedelta

def authorization(func):
    def inner(request):
        try:
            tk = request.get_signed_cookie('ticket',salt='sufan')
        except:
            return redirect('/login/')
        if not tk:                                                
            return redirect('/login/')
        else:
            return func(request)
    return inner

# 展示首页
def home(request): 

        return render(request, 'home.html')

# 登录页
def login(request):
    # return HttpResponse('home界面')
    # return render(request,'home.html')
    # 处理用户请求,并返回内容
    # request: 用户请求相关的所有信息(对象)

    # httpResponse只显示字符串
    # return HttpResponse('shabi')

    # 导入render,自动找到模板路径下的home.html文件,读取内容并返回给用户
    # 模板路径的配置

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        #  用户POST提交的数据(请求)
        #  print(request.POST)
        # u = request.POST['user']   这样的话如果别人写的不是user就会报错,用get没用就None而已
        # p = request.POST['pwd']

        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # if u == 'root' and p == '123123':
        #     # return redirect('http://www.baidu.com')
        #     return redirect('/manager/')
        # else:
        #     return render(request, 'login.html', {'msg': '用户名或密码错误!'})

        user = db_call.get_list('select name from user where ID=%s and pwd=%s ',[u,p,])

        if user:
            print(user)
            # return redirect('/manager/')
            obj = redirect('/manager/')
            # obj.set_cookie('ticket','sufansufan',max_age=10)            #   max_age = 10 超时时间10秒
            # ct = datetime.datetime.utcnow()                                             #   取得当前时间
            # v = timedelta(seconds =10)                                                      #   间隔
            # value = ct + v                                                                              #   计算到期日期
            # print(value)
            # obj.set_cookie('ticket','sufansufan',expires=value,secure=True)            #   max_age = 10 超时时间10秒
                                                                                                                #   path参数：设置cookie只在哪个路径生效
            # obj.set_signed_cookie('ticket', 'sufansufan', expires=value,salt='sufan')   #   secure参数是针对https的
            obj.set_signed_cookie('ticket', 'sufansufan', max_age=10,salt='sufan')   #   secure参数是针对https的
            # print(obj)
            return obj
        else:
            print('没有鸭')
            return render(request, 'login.html', {'msg': '用户名或密码错误!'})

# 后台管理页面
@authorization
def  manager(request):  #request 表示请求的所有相关信息
    # tk = request.COOKIES.get('ticket')  #   设置cookie
    # print(tk)

    # tk = request.COOKIES.get('ticket') 
    # try:
    #     tk = request.get_signed_cookie('ticket',salt='sufan')
    # except:
    #     return redirect('/login/')
    # if not tk:                                                 #    有cookie才给manager页面，没有返回login页面
    #     return redirect('/login/')
    # else:
        return render(request,'manager.html')

# 数据接收url
def  data_test(request):
    recv1 = request.POST.get('type')
    recv2 = request.POST.get('AT')
    recv3 = request.POST.get('param')
    print(recv1)
    print(recv2)
    print(recv3)
    # 获取时间值并格式化
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    db_call.modify('insert into command_log values(%s, %s,%s,%s)',[recv1,recv2,recv3,now_time])
    # return HttpResponse('OK!I accepted!')
    return JsonResponse({'result':200})  # 返回固定的Json字符串


# 指令记录展示页面
# @authorization
def show_info(request):
    command_list = db_call.get_list('select * from command_log order by time desc ',[])
    return render(request,'show_info.html',{'command_list':command_list})

def edit(request):
    return HttpResponse('hhh')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/',home),                      #  首页
    path('login/',login),                        #  登录页
    path('db_view/',db.db_view),       #  数据库展示页
    path('manager/',manager),           #  管理员后台页面
    path('dt/',data_test),                      #  指令上传指定url
    path('show_info/',show_info),     #  历史指令记录展示页面
    path('edit/(\w+).html',edit)           # 动态路由的设置，正则
]
