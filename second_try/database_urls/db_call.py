import pymysql

# 数据库语句调用

def get_list(sql,args):
    conn = pymysql.connect(host='localhost', user='root',
                           password='712688', database='208_robot', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_one(sql,args):
    conn = pymysql.connect(host='localhost', user='root',
                           password='712688', database='208_robot', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def modify(sql,args):
    conn = pymysql.connect(host='localhost', user='root',
                           password='712688', database='208_robot', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    conn.commit()
    cursor.close()
    conn.close()
