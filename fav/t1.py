import sqlite3

connect = sqlite3.connect('fav.db')
cursor = connect.cursor()

# 创建表
# 创建一个名为 favdb 的表，包含 id（自增主键）、name 和 url 字段
cursor.execute('''
CREATE TABLE IF NOT EXISTS favdb (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    url TEXT NOT NULL
)
''')
# 提交事务
connect.commit()


# 插入数据
def insert_data(name, url):
    """插入数据"""
    cursor.execute('''
    INSERT INTO favdb (name, url) VALUES (?, ?)
    ''', (name, url))
    connect.commit()  # 每次数据操作后提交事务


def remove_data(data_id):
    """删除数据"""
    cursor.execute('''
    DELETE FROM favdb WHERE name = ?
    ''', (data_id,))
    connect.commit()  # 每次数据操作后提交事务


def query_alldata():
    """查询数据"""
    cursor.execute('SELECT * FROM favdb')
    rows = cursor.fetchall()
    return rows  # 返回所有数据


# 关闭连接函数
def close_connection():
    """关闭数据库连接"""
    if connect:
        connect.close()


if __name__ == '__main__':
    # 示例操作
    insert_data('百度', 'baidu.com')
    # print(query_alldata())
    # remove_data('百度')
    # print(query_alldata())
    # close_connection()
    # pass

    # 可以在这里批量导入或者批量删除收藏夹