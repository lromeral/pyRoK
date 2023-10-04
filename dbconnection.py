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
    def insert_scandata_row (self,idscan:int,data:datos_reporte):
        cur = self.conn.cursor()
        sql = """INSERT INTO 
            scandata 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        new_row = [idscan].append(data.to_list())
        cur.execute(sql,new_row) 

    def get_conn (self):
        return self.conn

class vuelca_datos_db():
    def __init__(self) -> None:
        pass
    def start(self, bd_username, bd_pass, bd_name, server_ip, server_port, csv_path):
        #conn = conn_bd(bd_name,'rok#12345.','192.168.10.112',3306,'rok').get_conn()
        conn = conn_bd(bd_username,bd_pass,server_ip,server_port,bd_name).get_conn()
        origen_filename = csv_path
        filename = os.path.basename(origen_filename)
        filename = os.path.splitext(filename)[0]
        datetime_string = filename[:15]
        print (datetime_string)
        idscan = 0
        done = False
        try:
            cur = conn.cursor()
            kd = self.get_reino_from_filename(filename)
            timestamp = datetime.strptime(datetime_string,'%Y%m%d_%H%M%S')
            cur.execute("INSERT INTO scans (KD,scan_time) VALUES(?,?)", (kd,timestamp))
            cur.execute("SELECT * from scans where kd =? and scan_time =?",(kd,timestamp))

            rows = cur.fetchall()
            for r in rows:
                idscan = r[0]
            with open (file = origen_filename,mode='r', newline='', encoding="utf-8") as f:
                datos_origen = csv.reader(f)
                #Header
                datos_origen.__next__()

                for row in datos_origen:
                    data = datos_reporte(row)
                    #Evita inactivos
                    if data.id > 0:
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
                        print (f"Insertando jugador: {data.name}")
                        sql = """INSERT INTO 
                                scandata 
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        cur.execute(sql,new_row)

                conn.commit()
                conn.close()
            
            done = True
        except Exception as e:
            print (f"Error: {e}")
            done = False
            conn.rollback()

        if (done):
            dest_filename = os.path.dirname(origen_filename) + "/" + os.path.splitext(os.path.basename(origen_filename))[0] + "_ok.csv"
            os.rename(origen_filename,dest_filename)

    def get_reino_from_filename(self,filename:str)->str:
        result = filename[16:20]
        return result

