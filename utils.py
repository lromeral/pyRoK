import pyautogui as pa
import cfg  
import time
import csv
import os
import pytesseract
from itertools import groupby
from coords import coords
from PIL import Image, ImageGrab, ImageEnhance
from mylogger import getmylogger
from jugador import jugador
import cv2
import numpy as np
from telegram import telegram_notify
from datetime import datetime
    
moverA = pa.moveTo
obtener_posicion = pa.position
pauto=pa
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
logger = getmylogger(__name__)
notify = telegram_notify()

def click_on_location (loc:cfg._point)->bool:
    logger.debug (click_on_location.__name__)
    pa.moveTo(loc)
    click()
    time.sleep(0.3)
    return True   



def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def capture_region(loc:cfg.location, prepare:bool=False)->Image:
    logger.debug (capture_region.__name__)
    captura = ImageGrab.grab(bbox=loc)
    if prepare: captura = prepare_image(captura)
    return captura

def prepare_image (img_in:Image)->Image:
    img_out = cv2.cvtColor(np.array(img_in), cv2.COLOR_BGR2GRAY)
    img_out = cv2.threshold(img_out, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return img_out

def check_screeen (region_in,titulo:str)->bool:
    logger.debug(check_screeen.__name__)
    logger.debug(f"check_screen buscando:{titulo}")
    retry = 0
    retry_max = 5
    while True:
        if datos_alfanumericos(capture_region(region_in,True)) == titulo: 
            logger.debug(f"check_screen encontrada:{titulo}")
            return True
        else:
            if retry < retry_max:
                logger.warning(f"Reintenado check_screen {retry}")
                retry+=1
                time.sleep(retry)
            else:
                logger.error(f"check_screen no encontrada:{titulo}")
                return False



def screenshot (strPath:str)->Image:
    logger.debug (screenshot.__name__)
    logger.info ("Capturando pantana en " + strPath)
    return pa.screenshot(strPath,region=cfg.regions['screenshots'])

def guardar_imagen (img:Image, path:str, nombre:str)->bool:
    logger.debug (guardar_imagen.__name__)
    logger.info (f"Guardando imagen {nombre} en {path}") 
    if not os.path.exists(path): crearCarpeta (path)
    img.save (path + "/" + nombre)

def click (time_pressed:float=0.2)->None:
    logger.debug (click.__name__)
    time.sleep(0.3)
    pa.click(duration=time_pressed)
    time.sleep(0.3)

def crearCarpeta(path:str):
    logger.debug (crearCarpeta.__name__)
    logger.info  ("Creando carpeta en: " + path)
    try:
        os.mkdir(path)
    except:
        logger.critical ("No se pudo crear el directorio " +  path)
        salir("No se pudo crear el directorio")

def write_to_csv(data:list, fichero, header:list):
    logger.debug (write_to_csv.__name__)
    if (not os.path.exists(fichero)):
        logger.info ("Creando fichero csv")
        file = open (file = fichero ,mode='w', newline='', encoding="utf-8")
        wr = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
        wr.writerow(header)
        wr.writerow(data)
    else:
        file = open (file = fichero ,mode='a', newline='', encoding="utf-8")
        logger.info ("Guardando datos en fichero csv")
        wr = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
        wr.writerow(data)

#Devuelve los datos obtenidos sobre la alizanza
def datos_alfanumericos(img:Image)->str:
    logger.debug (datos_alfanumericos.__name__)
    datos = pytesseract.image_to_string(img, config=cfg.TESSERACT['ALPHANUMERIC']).strip()
    #return datos if len(datos) > 3 else "#error#"
    return datos

#Devuelve los datos obtenidos sobre la id de jugador
def datos_numericos(img:Image)->int:
    logger.debug (datos_numericos.__name__)
    #cv2.imshow('test',img)
    #cv2.waitKey(0)
    datos = list([])
    intentos = 0
    while True:
        intentos +=1
        lecturas = 3
        for lectura in range(1,lecturas):
            datos.append(((pytesseract.image_to_string(img,config=cfg.TESSERACT['ONLY_NUMBERS']).strip())))
            time.sleep(0.1)
        if intentos >10: 
            print ("No se consiguo el dato")
            salir("No se encuentra el dato numerico")
        else:
            if all_equal(datos):
                break 

    #print (f"Datos:{datos}")
    return int(datos[0]) if (datos[0].isnumeric() and datos[0]==datos[1]) else -1

def get_dato_alfanumerico(region, count:int, data:jugador, capturar:bool=False)->str:
    logger.debug (get_dato_alfanumerico.__name__)
    intentos=0
    max_intentos = 10
    datos_recogidos=list([])
    while True:
        for x in range (0,count):
            captura = capture_region(region=region)
            #captura.show()
            #input()
            #guardar_imagen(captura, cfg.paths['screenshots'] + str(data.kd), str(data.pos) + "_" +str(data.timestamp) + ".png")
            datos_recogidos.append(datos_alfanumericos(captura))
            logger.debug ("fCaptura #{x}: {datos_recogidos}")
        if not all_equal (datos_recogidos):
            if(intentos > max_intentos): 
                logger.critical ("No se puede obtener el dato")
                salir()
            else:
                datos_recogidos.clear()
                intentos +=1
        else:
            return datos_recogidos[0]

def get_dato_numerico(region, count:int, data:jugador, capturar:bool=False)->int:
    logger.debug (get_dato_numerico.__name__)
    intentos=0
    max_intentos = 10
    datos_recogidos = list([])
    while True:
        for x in range (0,count):
            captura:Image = capturar_region(region=region).convert('L')
            #captura.show()
            #input()
            #guardar_imagen(captura, cfg.paths['screenshots'] + str(data.kd), str(data.pos) + "_" + str(data.timestamp)  + ".png")
            datos_recogidos.append (datos_numericos(captura))
            logger.debug (f"Captura #{x}: {datos_recogidos}")
        if not all_equal (datos_recogidos) or datos_recogidos[0] == -1:
            if(intentos > max_intentos): 
                logger.critical ("No se puede obtener el dato")
                salir()
            else:
                datos_recogidos.clear()
                intentos +=1
        else:
            return datos_recogidos[0]

def is_ventana (region:str ,titulo:str)->bool:
    logger.debug (is_ventana.__name__)
    
    lectura = get_dato_alfanumerico(region,3).casefold()
    logger.debug("Lectura Pantalla: " + lectura)
    return lectura == titulo.casefold()

#Aborta el programa con mensaje en consola
def salir (mensaje:str=""):
    logger.debug (salir.__name__)
    notify.send_message (f'Programa abortado a las {datetime.now()}. Razón: {mensaje}')
    exit(-1)


def capture_cv(loc):
    logger.debug (capture_region.__name__)
    captura = ImageGrab.grab(bbox=loc)
    captura = cv2.cvtColor(np.array(captura), cv2.COLOR_RGB2BGR)
    norm_img = np.zeros((captura.shape[0], captura.shape[1]))

    cv2.imshow("hola",norm_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
