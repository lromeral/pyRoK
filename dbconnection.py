# Module Imports
import mariadb
import sys
from datetime import datetime
import csv
from datos_reporte import datos_reporte
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="rok",
        password="rok#12345.",
        host="192.168.10.112",
        port=3306,
        database="rok"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

def get_reino_from_filename(filename:str)->str:
    result = filename[:filename.find("_")]
    return result

#origen_filename = '3135_20230912_185502_data.csv'
origen_filename = '3131_20230922_205830_data.csv'

datetime_string = origen_filename[origen_filename.find("_")+1:origen_filename.find("d")-1]
print (datetime_string)
idscan = 0
cur = conn.cursor()
kd = get_reino_from_filename(origen_filename)


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


