import time
from datetime import datetime
from scan import scan
import utils as u
import cfg as c
import os
from capture_screenshots import captura_screenshots
from telegram import telegram_notify

if __name__=='__main__':
    kd = input("Nombre del Reino: ")
    i = int (input("Inicio: "))
    f = int(input('Final: ')) +1
    time.sleep(5)
    m = captura_screenshots(kdname=kd, inicio=i ,final=f)
    comienzo = datetime.utcnow()
    m.logger.info (comienzo)
    
    m.start()
    
    final = datetime.utcnow()
    m.logger.info (final)
    tiempo_total = final - comienzo
    notify = telegram_notify()
    notify.send_message(f'Captura finalizada en: {tiempo_total}')
    m.logger.info (f"Tiempo transcurrido: {tiempo_total}")
    





