import pymysql
import configparser 

config = configparser.ConfigParser()
config.read('../Chapter1/config.ini')


# 特例 -> 因為 CREATE DATABASE 不能帶入字串
def create_database(database):
    connection = pymysql.connect(
        host=config.get('DB', 'host'),
        user=config.get('DB', 'user'),
        password=config.get('DB', 'password'),
        port=config.getint('DB', 'port'),
        cursorclass=pymysql.cursors.DictCursor,
    )
    # 用兩個 ** (會變成一個 dict)可以直接把 connection 整串帶入

    with connection.cursor() as cursor:
    # 要加入 %s 所以要把下面原本的 f"" 要拿掉(把 f 刪除)
    # 可是如果用 %s 用法，在帶入 2-4 時，SQL 會認定用了字串建立 table，所以這邊建議用 f"" 建立表格
        sql = f"""
            CREATE DATABASE IF NOT EXISTS {database};
        """
    # 執行建立的 SQL 語句
        cursor.execute(sql) # 把 %s 的參數放這行 -> database
    # 執行查看資料庫
        cursor.execute("SHOW DATABASES;")
        dbs = cursor.fetchall()

    print(dbs)


def create_user_table(database):
    connection = pymysql.connect(
        host=config.get('DB', 'host'),
        user=config.get('DB', 'user'),
        password=config.get('DB', 'password'),
        port=config.getint('DB', 'port'),
        cursorclass=pymysql.cursors.DictCursor,
        database=database,
)
    with connection.cursor() as cursor:
        sql = """
            CREATE TABLE IF NOT EXISTS user (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(200) NOT NULL,
                age INT,
                username VARCHAR(200) NOT NULL UNIQUE,
                password VARCHAR(200) NOT NULL);
    """
        cursor.execute(sql)
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
    print(tables)

# 建立寫入使用者的 function
def create_user(name, age, username, password, database='chapter2'):
    connection = pymysql.connect(
        host=config.get('DB', 'host'),
        user=config.get('DB', 'user'),
        password=config.get('DB', 'password'),
        port=config.getint('DB', 'port'),
        cursorclass=pymysql.cursors.DictCursor,
        database=database
    )
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO user (name, age, username, password)
            VALUES (%s, %s, %s, %s);
         """
        cursor.execute(sql,(name, age, username, password))
        cursor.execute("SELECT * FROM user;")
        r = cursor.fetchall() 
    connection.commit()


# 查詢使用者的 function


# 建立寫入使用者的 function