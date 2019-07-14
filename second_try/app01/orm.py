from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse


# 多表查询获取
# views.py中
# from django.db import models
#
# class Foo(models.Model):
#     caption = models.CharField(max_length=16)
#
# class UserType(models.Model):
#     title = models.CharField(max_length=32)
#     fo = models.ForeignKey('Foo',on_delete=models.CASCADE)
#
# class UserInfo(models.Model):
#     name = models.CharField(max_length=16)
#     age = models.IntegerField()
#     ut = models.ForeignKey('UserType',on_delete=models.CASCADE)
#


# QuerySet[obj,obj,obj]
# result = models.UserInfo.objects.all()
# for obj in result:
#     print(obj.name,obj.age,obj.ut_ID,obj.ut.title)

# UserGroup ,ut是FK字段--正向操作    # 一个用户只有一个用户类型
# obj = models.UserInfo.objects.all.first()
# print(obj.name,obj.age,obj.ut.title)

# UserType,表中小写_set.all() --反向操作  # 一个用户类型下可以有很多用户
# .values__   没有set
# obj = models.UserType.objects.all().first()
# print('用户类型',obj.id,obj.title)
# for row in obj.UserInfo_set.all():
#     print(row.name,row.age)

#     result = models.UserType.objects.all()
#     for item in result:
#         print(item.title,item.userinfo_set.all())   # 打印用户类型，后一个打印该类型下的所有用户
#         print(item.title,item.userinfo_set.filter(name='xxx'))


# 分页

# 分批获取数据
#   models.UserInfo.objects.all()[0:10]
#   models.UserInfo.objects.all()[10:20]


# django自带的分页功能
from app01 import models


def index(request):

    # # 创造数据
    # for i in range(300):
    #   name = 'root'+str(i)
    #   models.UserInfo.objects.create(username=name,age=18,password=123)
    current_page = request.GET.get('page')
    print(current_page)
    # current_page = int(current_page)
    # 要排序，不然会出错：UnorderedObjectListWarning: Pagination may yield inconsistent
    # results
    user_list = models.UserInfo.objects.all().order_by('nid')
    from django.core.paginator import Paginator, Page
    paginator = Paginator(user_list, 10)
    # per_page:每页显示条目数量
    # count： 数据总个数
    # num_pages: 总页数的索引范围,eg:(1,10)
    # page: page对象
    posts = paginator.page(current_page)
    # has_next                      是否有下一页
    # next_page_number     下一页页码
    # has_previous              是否有上一页
    # previous_page_number  上一页页码
    #  object_list                          分页之后的数据列表
    # number                        当前页
    # paginator                     paginator对象
    return render(request, 'index_orm.html', {'posts': posts})

# 自定义分页


# def custom(request):
#     # 用户当前想要访问的页码：8
#     current_page = request.GET.get('page')
#     current_page = int(current_page)
#     # 每页显示数据个数
#     per_page = 10
#     # 1 0:10
#     # 2 10:20
#     # 3 20:30
#     start = (current_page - 1) * per_page
#     end = current_page * per_page
#
#     user_list = models.UserInfo.objects.all()[start:end]
#     return render(request, 'custom.html', {'user_list': user_list})


# 改进
class PageInfo(object):

    def __init__(self, current_page, all_count,
                 per_page, base_url, show_page=11):
        '''
        :param current_page:    当前页码数
        :param all_count:            数据库总行数
        :param per_page:           每页显示的行数
        :param base_url:              获取基本url,后面就可以加上?page=xx
        :param show_page:        想要显示11页就好，不要一次性30多页这么多

        '''
        # 获得当前页码，如果用户在url上面直接输入负数、文字、字母，超过页数等就直接当作第一页
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1

        self.per_page = per_page            #每页显示的行数
        # 拿从数据库拿出来的总共有的行数和每页要显示的相除，如果有余数(即b!=0),就加一面
        a, b = divmod(all_count, per_page)  # 得到除数，余数，eg：divmod(7,2)，则a=3，b=1
        if b:
            a = a + 1

        self.all_pager = a                              # 定义计算出来的所需要显示的总页数
        self.show_page = show_page       #  声明：需要展示的11页就好，不要一次性30多页这么多
        self.base_url = base_url                  # 声明：获取基本url,后面就可以加上?page=xx

    # 每一页显示的开始数据在第几行,方便后面调用,生成的list
    def start(self):
        return (self.current_page - 1) * self.per_page

    # 每一页显示的结束数据在第几行,方便后面调用,生成的list
    def end(self):
        return self.current_page * self.per_page

    # 定义分页栏方法
    def pager(self):
        # 空列表存储显示的每一个标签,上一页标签,1,2,3,4,5......10,11,下一页标签
        page_list = []
        # 定义分页栏的中间数值,因为show_page=11，所以这里是5
        half = int((self.show_page - 1) / 2)

        '''
        首先判断如果要显示的数据并没法大于11页,每页10行这么多的量,
        即如果数据总页数<11
        '''
        if self.all_pager < self.show_page:
            begin = 1
            end = self.all_pager + 1
        # 否则数据量够大
        else:
            # 判断如果当前页<=5,分页栏就不需要变动,一直显示1到11
            if self.current_page <= half:
                begin = 1
                end = self.show_page + 1
            # 如果当前页>=6，分页栏变动，变动为当前页少5页和多5页的区间
            else:
                # 如果当前页+half页就比最后一页还大的话：固定最后的分页栏
                if self.current_page + half > self.all_pager:
                    begin = self.all_pager - self.show_page + 1
                    end = self.all_pager + 1
                else:
                    begin = self.current_page - half
                    end = self.current_page + half + 1
        # 制作上一页标签
        # 如果当前页就是第一页的话，#就不跳转
        if self.current_page <= 1:
            prev = "<li><a  href='#'>上一页</a></li>"
        else:
            prev = "<li><a  href='%s?page=%s'>上一页</a><li>" % (
                self.base_url, self.current_page - 1,)
        # 将上一页标签添加到列表
        page_list.append(prev)

        # 前面得到了当前应该要显示的begin,end,开始遍历
        for i in range(begin, end):
            if i == self.current_page:
                # 当前页面编号的bootstrap加个背景
                temp = "<li class='active'><a href='%s?page=%s'>%s</a></li>" % (
                    self.base_url, i, i,)
            else:
                temp = "<li><a href='%s?page=%s'>%s</a></li>" % (
                    self.base_url, i, i,)
            page_list.append(temp)

        # 制作下一页标签
        if self.current_page >= self.all_pager:
            next = "<li><a  href='#'>下一页</a></li>"
        else:
            next = "<li><a  href='%s?page=%s'>下一页</a></li>" % (
                self.base_url, self.current_page + 1,)
        page_list.append(next)
        # 合并标签,一起送给前端
        return ''.join(page_list)


def custom(request):
    all_count = models.UserInfo.objects.count()   # 得到数据库总行数

    page_info = PageInfo(
        request.GET.get('page'),
        all_count,
        10,
        '/app01/custom/')
    user_list = models.UserInfo.objects.all()[
        page_info.start():page_info.end()]
    return render(request, 'custom.html', {
                  'user_list': user_list, 'page_info': page_info})
