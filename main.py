import time
from datetime import datetime
from scan import scan
import utils as u
import cfg as c
import os
from procesa_imagenes import procesa_imagenes
from capture_screenshots import captura_screenshots
from telegram import telegram_notify
from dbconnection import vuelca_datos_db

if __name__=='__main__':
    kd = input("Nombre del Reino: ")
    i = int (input("Inicio: "))
    f = int(input('Final: ')) +1
    time.sleep(5)

    m = captura_screenshots(kdname=kd, inicio=i ,final=f)
    p = procesa_imagenes()
    d = vuelca_datos_db()

    comienzo = datetime.utcnow()
    m.logger.info (comienzo)
    
    server_ip = 'rok.foromtb.com'
    server_port = 43306


    #p.start (dir_in='20231004_080515_3129',dir_out=None,inicio=299,final=300)
    #d.start('rok','rok#12345.','rok',server_ip,server_port,'./scans/20231004_080515_3129/20231004_080515_3129.csv')
    
    if m.start(): 
        if p.start(m.get_scan_folder(),'',i,f):
            d.start('rok','rok#12345.','rok',server_ip,server_port,p.get_csv_path())
        else:
            u.salir("No finalizó correctamente el volcado de datos")  
    else:
        u.salir("No finalizó correctamente la captura de pantallas")   
    
    final = datetime.utcnow()
    m.logger.info (final)
    tiempo_total = final - comienzo
    notify = telegram_notify()
    notify.send_message(f'Captura finalizada en: {tiempo_total}')
    m.logger.info (f"Tiempo transcurrido: {tiempo_total}")
    