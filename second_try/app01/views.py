from django.shortcuts import render

# Create your views here.

from django.shortcuts import  HttpResponse
# 数据库相关操作
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
