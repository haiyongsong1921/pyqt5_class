import sqlite3


def creatSQLiteDataBase(dbName):
    connection = sqlite3.connect(dbName)
    return connection

def createTable(connection, tableName):
    cursor = connection.cursor()
    sql = 'create table IF NOT EXISTS {0}(id int(11) primary key, name varchar(30), class varchar(10), school varchar(20))'.format(tableName)
    cursor.execute(sql)
    return cursor
'''
    sqlClause = 'insert into student values (1, "Vincent", "三年二班", "八中")'
    cursor.execute(sqlClause)
    sqlClause = 'insert into student values (2, "Jay", "三年二班", "八中")'
    cursor.execute(sqlClause)
    sqlClause = 'insert into student values (3, "Sophia", "三年二班", "八中")'
    cursor.execute(sqlClause)
'''

DATABASE_NAME = 'STEAM.db'
if __name__ == '__main__':
    connection = creatSQLiteDataBase(DATABASE_NAME)
    cursor = createTable(connection, 'student')
    cursor.execute('select * from student')

    result = cursor.fetchone() #返回一条记录
    print(result)
    result2 = cursor.fetchmany(2) #返回多条记录
    print(result2)

   # result5 = cursor.fetchall()  # 返回全部记录R
   # print(result5)

    cursor.close()
   # connection.commit()
    connection.close()