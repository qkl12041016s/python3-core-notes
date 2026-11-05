import os

import pymongo
import pymysql

# 凭据从当前运行环境读取。
with pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    connect_timeout=5,
) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        print(cursor.fetchone()[0])

# 客户端退出上下文时关闭连接资源。
with pymongo.MongoClient(
    os.environ["MONGO_URI"], serverSelectionTimeoutMS=5000
) as client:
    print(client.admin.command("ping")["ok"])
