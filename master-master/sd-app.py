import time, sys
import MySQLdb as mdb

#10.7.0.51 10.7.0.52
con1 = mdb.connect(host="10.7.0.51", user="app", passwd="123456", db="teste")
con2 = mdb.connect(host="10.7.0.52", user="app", passwd="123456", db="teste")

cur1 = con1.cursor()
cur2 = con2.cursor()

request_for_second = int(sys.argv[1])

start = int(round(time.time() * 1000))
end = 0

while(end - start < 60000):
    for i in range(20):
        cur1.execute("Insert Into teste (numero, teste) Values (" + str(i) +",'testando')" )
        con1.commit()
        
        cur2.execute("Delete FROM teste Where numero=" + str(i))
        con2.commit()

#        time.sleep(1.0/request_for_second)

    end = int(round(time.time() * 1000))

con1.close()
con2.close()
