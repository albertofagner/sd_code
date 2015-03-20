import time, sys
import MySQLdb as mdb

#10.7.0.51 10.7.0.52
con_m = mdb.connect(host="10.7.0.51", user="app_bench", passwd="123456", db="teste")
con_s = mdb.connect(host="10.7.0.52", user="app_bench", passwd="123456", db="teste")

cur_m = con_m.cursor()
cur_s = con_s.cursor()
tempo_m = []
tempo_s = []

start = int(round(time.time() * 1000))
for i in range(20):
    start_m = int(round(time.time() * 1000))
    cur_m.execute("Select * from teste")
    tempo_m.append(int(round(time.time() * 1000)) - start_m)

    start_s = int(round(time.time() * 1000))
    cur_s.execute("Select * from teste")
    tempo_s.append(int(round(time.time() * 1000)) - start_s)


print sum(tempo_m)/(len(tempo_m)*1.0)
print sum(tempo_s)/(len(tempo_m)*1.0)

con_m.close()
con_s.close()
