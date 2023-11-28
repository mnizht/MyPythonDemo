import psycopg2
from psycopg2 import sql
from datetime import datetime, timedelta
import random
import string

# 设置数据库连接参数
db_params = {
    'dbname': 'SpringTest',
    'user': 'postgres',
    'password': 'postgres123',
    'host': '172.27.21.165',
    'port': '5432'
}

# 连接到 PostgreSQL 数据库
conn = psycopg2.connect(**db_params)

# 创建一个游标对象
cur = conn.cursor()

# 定义插入批次大小
batch_size = 1000

# 生成测试数据并插入表中
for i in range(1, 1000001):
    org_id = random.randint(1, 100)

    # 生成随机的日期和时间
    random_date = datetime(2020, 1, 1) + timedelta(days=random.randint(0, (datetime.now() - datetime(2020, 1, 1)).days))
    random_time = timedelta(seconds=random.randint(0, 86400))  # 86400 秒是一天的秒数
    patrol_time = random_date + random_time

    remark = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(64))  # 随机生成字符串

    # 有一定概率将 remark 设置为 NULL
    if random.random() < 0.1:
        remark = None

    # 插入数据
    insert_query = sql.SQL('''
        INSERT INTO patrol_record (org_id, patrol_time, remark) 
        VALUES (%s, %s, %s)
    ''')
    cur.execute(insert_query, (org_id, patrol_time, remark))

    # 每插入 batch_size 条记录提交一次事务
    if i % batch_size == 0:
        conn.commit()
        print(f'Inserted {i} records.')

# 提交事务（确保最后一批数据也被提交）
conn.commit()

# 关闭连接
cur.close()
conn.close()
