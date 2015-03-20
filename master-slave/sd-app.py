import time, sys
import MySQLdb as mdb

#10.7.0.43 10.7.0.47
con = mdb.connect(host="10.7.0.43", user="app", passwd="123456", db="teste")

cur = con.cursor()

request_for_second = int(sys.argv[1])

start = int(round(time.time() * 1000))
end = 0

while(end - start < 60000):
    for i in range(20):
        cur.execute("Insert Into Teste (numero, nome) Values (" + str(i) +",'testando')" )
        con.commit()
#        time.sleep(1.0/request_for_second)

    for i in range(20):
        cur.execute("Delete FROM Teste Where numero=" + str(i))
        con.commit()
 #       time.sleep(1.0/request_for_second)

    end = int(round(time.time() * 1000))

con.close()
