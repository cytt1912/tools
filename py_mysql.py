import time
import uuid

import pymysql

db = pymysql.connect("localhost","root","cytlovedll","test")
cursor = db.cursor()
for i in range(1000):
    cursor.execute("insert into goods values ('%s','%s','%s')"
                   %(300 + i, uuid.uuid1().hex, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
db.commit()
