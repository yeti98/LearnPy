import pymysql

class Connector:
    def __init__(self):
        pass

    def getConnect(self):
        fpointer = open('../../data/acc.txt')
        host = fpointer.readline()[:-1];
        user = fpointer.readline()[:-1];
        pwd = fpointer.readline()[:-1];
        db = fpointer.readline();
        fpointer.close()
        return pymysql.connect(host=host,
                             user=user,
                             password=pwd,
                             db=db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

connection = Connector().getConnect();
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM news_resource LIMIT 15"
        cursor.execute(sql)
        # print("cursor.description: ", cursor.description)
        for row in cursor:
            print(row)
finally:
    connection.close()


