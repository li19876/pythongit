import pymysql
import time
db = pymysql.Connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
cursor = db.cursor()
item= {"city":"aaaa","trade":"sdasda","frname":"sdasd","gsname":"sdasd","phone":"Dasda"}
sql = """
    insert into customer(city,trade,frname,gsname,phone,timestamp) values ('{}','{}','{}','{}','{}','{}')
""".format(item["gsname"][0:2],item["trade"],item["frname"],item["gsname"],item["phone"],int(time.time()))

print("开始写入")
cursor.execute(sql)
res=db.commit()

print(res)

cursor.close()
db.close()
