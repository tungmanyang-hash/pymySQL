# 引入所需套件
import pymysql
from configparser import ConfigParser
# 讀取 config.ini 檔案取得資料庫連線資訊
config = ConfigParser()
config.read('config.ini')


class SqlUtils:
    db_query = "SHOW DATABASES;"


    def __init__(self, database=None):
        self.connection = pymysql.connect(
            host=config['DB']['host'],
            user=config['DB']['user'],
            password=config['DB']['password'],
            port=int(config['DB']['port']),
            cursorclass=pymysql.cursors.DictCursor,
            database=database
    )
    
    def sql_query(self, query):
    # 建立 function 執行 SQL 查詢
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        return result

    def show_dbs(self):
    # 建立 function 執行 SQL 查詢
        with self.connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES;")
            result = cursor.fetchall()

        return result