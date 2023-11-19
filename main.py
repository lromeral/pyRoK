import time
from datetime import datetime
import utils
import get_data
import capture_data
from telegram import telegram_notify
import dbconnection
import navegacion

if __name__=='__main__':
    notify = telegram_notify()
    kd_inicio = int(input("Nombre del Reino de Inicio: "))
    kd_final = int(input("Nombre del Reino de Final: "))
    hora_inicio = int(input("Hora de inicio (-1 para empezar ahora): "))
    minuto_inicio = int(input("Minuto de inicio (0..59): "))

    if (hora_inicio>23): hora_inicio = 0
    if (minuto_inicio>59): minuto_inicio=0


    if (hora_inicio != -1):
        while (True):
            tiempo_actual = datetime.now()
            if (tiempo_actual.hour == hora_inicio and tiempo_actual.minute==minuto_inicio):
                break
            else:
                print ("Esperando a la hora programada.")
                print (tiempo_actual)
                time.sleep(15)

    posicion_inicial = 1
    posicion_final = 300

    for reino in range (kd_inicio,kd_inicio + 1):
        kd = reino
        i = posicion_inicial
        f = posicion_final +1
        
        comienzo = datetime.utcnow()
        utils.logger.info (comienzo)
        notify.send_message(f'[{reino}] comienza: {comienzo}')
        
        time.sleep(5)
        navegacion.abrir_reino (reino)
        time.sleep(5)

        m = capture_data.capture_data(kdname=kd, inicio=i ,final=f)
        g = get_data.get_data()
        d = dbconnection.vuelca_datos_db()


        
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
                notify.send_message(f'[{reino}] error en el volcado de datos')
                utils.salir("No finalizó correctamente el volcado de datos")  
        else:
            notify.send_message(f'[{reino}] error en la captura de pantallas')
            utils.salir("No finalizó correctamente la captura de pantallas")   
        final = datetime.utcnow()
        m.logger.info (final)
        tiempo_total = final - comienzo
        notify.send_message(f'[{reino}] finaliza: {final}. Tiempo total: {tiempo_total}')
        m.logger.info (f"Tiempo transcurrido: {tiempo_total}")
    