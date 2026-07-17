# 把這些打包成method

# 引入所需套件
import pymysql
from configparser import ConfigParser
# 讀取 config.ini 檔案取得資料庫連線資訊
config = ConfigParser()
config.read('config.ini')


class SqlUtils:
    db_query = "SHOW DATABASES;" # 把查詢的語句，寫在類別屬性裡面。有固定或是常用的語句，都可以寫在類別屬性裡。會變得很方便，不用一直重複打


    # 基於連線，才可以坐下面的操作。所以將 connection 寫在實例屬性，讓下面的 method 都可以用 self.connection 來取用這個實例屬性，做一些我們想做的操作
    def __init__(self, database=None): # 我沒給指定 database 時，就預設是 None
        self.connection = pymysql.connect(
            host=config['DB']['host'],
            user=config['DB']['user'],
            password=config['DB']['password'],
            port=int(config['DB']['port']),
            cursorclass=pymysql.cursors.DictCursor,
            database=database
    )
        # connection 如果寫在全域變數，要同時查詢多筆資料時，會發生衝突，因此寫在 function 裡比較好


    
    def sql_query(self, query):
    # 建立 function 執行 SQL 查詢
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        return result


    # 以下其實可以刪除了，因為已經把查詢寫成類別屬性打包進 sql_query 了
    #  db_query = "SHOW DATABASES;" --> 12行的這句，其實就是下面的簡寫了
    
    # 建立 function 執行 SQL 查詢
        with self.connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES;")
            result = cursor.fetchall()

        return result