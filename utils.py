import pyautogui as pa
import cfg  
import time
import csv
import os
import pytesseract
from itertools import groupby
from coords import coords
from PIL import Image, ImageGrab
from mylogger import getmylogger
from jugador import jugador
    
moverA = pa.moveTo
obtener_posicion = pa.position
pauto=pa
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
logger = getmylogger(__name__)

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def capturar_region(region)->Image:
    logger.debug (capturar_region.__name__)
    captura = ImageGrab.grab(bbox=region)
    return captura

def screenshot (strPath:str)->Image:
    logger.debug (screenshot.__name__)
    logger.info ("Capturando pantana en " + strPath)
    return pa.screenshot(strPath,region=cfg.regions['screenshots'])

def guardar_imagen (img:Image, path:str, nombre:str)->bool:
    logger.debug (guardar_imagen.__name__)
    logger.info (f"Guardando imagen {nombre} en {path}") 
    if not os.path.exists(path): crearCarpeta (path)
    img.save (path + "/" + nombre)

def click (time_pressed:float=0.1)->None:
    logger.debug (click.__name__)
    time.sleep(time_pressed)
    pa.click()
    time.sleep(time_pressed)

def crearCarpeta(path:str):
    logger.debug (crearCarpeta.__name__)
    logger.info  ("Creando carpeta en: " + path)
    try:
        os.mkdir(path)
    except:
        logger.critical ("No se pudo crear el directorio " +  path)
        exit(-1)

def is_screen(region, titulo_ventana:str, datos:jugador)->bool:
    logger.debug (is_screen.__name__)
    time.sleep(0.5)
    logger.info ("Identificando pantalla: " + titulo_ventana)
    intentos=0
    max_intentos = 5
    while (not is_ventana(region,titulo_ventana, datos) and intentos <= max_intentos):
        logger.warning ("Ventana no encontrada. Reintentando #" + str(intentos))
        intentos +=1
        time.sleep(5)

    if (intentos >= max_intentos):
        logger.critical ("Ventana no encontrada.")
        return False
    else:
        logger.info ("Ventana encontrada")
        return True
    
def procesar_pantalla(img:Image, nombre_ventana:str, hacer_click:bool=True)->coords:
    logger.debug (procesar_pantalla.__name__)
    if (not is_screen(img, nombre_ventana)):
        logger.critical ("Finalizando")
        exit(-1)
    else:
        zero = pa.locateOnScreen(img,confidence=cfg.scan['confidence'])
        logger.info ("Moviendo a imagen encontrada...")
        pa.moveTo(zero.left + zero.width/2, zero.top + zero.height/2,duration=3)
        if hacer_click:click()
        return coords((zero.left,zero.top))

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
    datos = pytesseract.image_to_string(img).strip()
    return datos if len(datos) > 3 else "#error#"

#Devuelve los datos obtenidos sobre la id de jugador
def datos_numericos(img:Image)->int:
    logger.debug (datos_numericos.__name__)
    datos =  (pytesseract.image_to_string(img,config=cfg.tesseract['cfg_only_numbers']).strip())
    return int(datos) if datos.isnumeric() else -1


def get_dato_alfanumerico(region, count:int, data:jugador, capturar:bool=False)->str:
    logger.debug (get_dato_alfanumerico.__name__)
    intentos=0
    max_intentos = 10
    datos_recogidos=list([])
    while True:
        for x in range (0,count):
            captura = capturar_region(region=region)
            #captura.show()
            #input()
            guardar_imagen(captura, cfg.paths['screenshots'] + str(data.kd), str(data.pos) + "_" +str(data.timestamp) + ".png")
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
            guardar_imagen(captura, cfg.paths['screenshots'] + str(data.kd), str(data.pos) + "_" + str(data.timestamp)  + ".png")
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

def is_ventana (region:str ,titulo:str, data:jugador)->bool:
    logger.debug (is_ventana.__name__)
    
    lectura = get_dato_alfanumerico(region,3,data).casefold()
    logger.debug("Lectura Pantalla: " + lectura)
    return lectura == titulo.casefold()

#Aborta el programa con mensaje en consola
def salir (mensaje:str=""):
    logger.debug (salir.__name__)
    #print (mensaje)
    exit(-1)