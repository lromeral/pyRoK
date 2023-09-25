# Module Imports
import mariadb
import sys
import os
from datetime import datetime
import csv
from datos_reporte import datos_reporte




class conn_bd:
    def __init__(self, dbuser:str, dbpass:str, dbhost:str, dbport:int,dbname:str) -> None:
    # Connect to MariaDB Platform
        try:
            self.conn = mariadb.connect(
                user=dbuser,
                password=dbpass,
                host=dbhost,
                port=dbport,
                database=dbname
        )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
    def exec
def get_reino_from_filename(filename:str)->str:
    result = filename[:filename.find("_")]
    return result

#origen_filename = '3135_20230912_185502_data.csv'
origen_filename = './reports_ok/3131_20230924_184114_data.csv'

for f in os.listdir():
    if os.path.isfile(f):


filename = os.path.basename(origen_filename)
filename = os.path.splitext(filename)[0]
datetime_string = filename[filename.find("_")+1:filename.find("d")-1]
print (datetime_string)
idscan = 0
cur = conn.cursor()
kd = get_reino_from_filename(filename)


timestamp = datetime.strptime(datetime_string,'%Y%m%d_%H%M%S')
cur.execute("INSERT INTO scans (KD,scan_time) VALUES(?,?)", (kd,timestamp))
conn.commit()

cur.execute("SELECT * from scans where kd =? and scan_time =?",(kd,timestamp))

rows = cur.fetchall()
for r in rows:
    idscan = r[0]




origen = open (file = origen_filename,mode='r', newline='', encoding="utf-8")
datos_origen = csv.reader(origen)

#Header
datos_origen.__next__()

for row in datos_origen:
    data = datos_reporte(row)
    new_row = [
        data.id,
        data.position,
        data.name,
        data.alliance,
        data.power,
        data.powerH,
        data.kp,
        data.deaths,
        data.rss_assist,
        data.t4kills,
        data.t5kills,
        data.timestamp
    ]
    fecha = datetime.utcfromtimestamp(data.timestamp)
    new_row[11] = fecha
    new_row.insert(0,idscan)

    print (new_row)


    sql = """INSERT INTO 
            scandata 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(sql,new_row)

conn.commit()


