from django.shortcuts import render,redirect
import pymysql
from django.db import connection


# 城市代码数据库展示页面
def db_view(request):
    conn = pymysql.connect(host='localhost', user='root',
                           password='712688', database='test_demo', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select * from city_code')
    code_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request,'db_view.html',{'city_code_list':code_list})