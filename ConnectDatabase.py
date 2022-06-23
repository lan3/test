import pymysql

'''
连接数据库，执行SQL
'''


# 连接数据库
def connect_database():
    # 主机，服务器
    host = 'test.smileteeth.cn'
    port = 3306
    username = 'root'
    password = 'Uatdb1234!'
    # 数据库
    database = 'tenant_10000_test'
    charset = 'utf8'
    # 建立数据库连接
    conn = pymysql.connect(host=host, port=port, user=username, passwd=password, db=database, charset=charset)
    # 创建游标，操作设置为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print("已连接数据库。")
    return conn, cursor


# 执行SQL命令
def execute_sql(conn, cursor, command, sql):
    sql = sql.encode('utf-8')
    # sql语句是查询
    if command in 'SELECT':
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print("已执行SQL。")
            return result
        except Exception as e:
            print("SQL命令执行失败！错误信息为：", e)
    # sql语句是添加，修改和删除
    elif command in ('INSERT', 'UPDATE', 'DELETE'):
        try:
            cursor.execute(sql)
            conn.commit()
            print("已执行SQL。")
        except Exception as e:
            conn.rollback()
            print("SQL命令执行失败！错误信息为：", e)
    else:
        print("SQL错误！")


# 关闭数据库
def close_database(conn, cursor):
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()
    print("已关闭数据库。")
