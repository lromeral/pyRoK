import time
from datetime import datetime
import utils as u
import get_data
import capture_data
from telegram import telegram_notify
import dbconnection

if __name__=='__main__':
    kd = input("Nombre del Reino: ")
    i = int (input("Inicio: "))
    f = int(input('Final: ')) +1
    time.sleep(5)

    m = capture_data.capture_data(kdname=kd, inicio=i ,final=f)
    g = get_data.get_data()
    d = dbconnection.vuelca_datos_db()

    comienzo = datetime.utcnow()
    m.logger.info (comienzo)
    
    server_ip = 'rok.foromtb.com'
    server_port = 43306


    #p.start (dir_in='20231004_174025_3150',dir_out=None,inicio=290,final=300)
    #d.start('rok','rok#12345.','rok',server_ip,server_port,'./scans/20231004_174025_3150/20231004_174025_3150.csv')
    #exit(-1)
    if m.start():
        if g.start(m.get_scan_folder(),'',i,f):
            d.start('rok','rok#12345.','rok',server_ip,server_port,g.get_csv_path())
            pass
        else:
            u.salir("No finalizó correctamente el volcado de datos")  
    else:
        u.salir("No finalizó correctamente la captura de pantallas")   
    final = datetime.utcnow()
    m.logger.info (final)
    tiempo_total = final - comienzo
    notify = telegram_notify()
    #notify.send_message(f'Captura finalizada en: {tiempo_total}')
    m.logger.info (f"Tiempo transcurrido: {tiempo_total}")
    