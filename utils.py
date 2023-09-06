import sys
sys.path.append('../')
import pyautogui as pa
import cfg  
import time
import csv
import os
import pytesseract
import math
from PIL import Image, ImageGrab


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class coords:
    __cords= (0,0)
    def __init__(self, x=(0,0)) -> None:
        self.__cords = x

    def set_coords(self, x):
        self.__cords=x

    def __eq__(self, __value: object) -> bool:
        return ((self.width == __value.width) and (self.height == __value.height)) 

    def __str__(self) ->str:
        return str(self.__cords)
    
    def distanciaAB(self, x1, x2, y1, y2) -> float:
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
     
    @property
    def width (self) -> float:
        return self.__cords[0]
    @property
    def height (self) -> float:
        return self.__cords[1]
    @property
    def center (self) -> tuple:
        return self.width/2, self.height/2

def capturar_region(region)->Image:
    captura = ImageGrab.grab(bbox=region)
    captura.show()
    return captura


def screenshot (strPath:str)->Image:
    print ("Capturando pantana en " + strPath)
    return pa.screenshot(strPath,region=cfg.regions['screenshots'])

def click ()->None:
    time.sleep(0.5)
    print ("Click!")
    pa.click()
    time.sleep(0.5)

def crearCarpeta(path:str):
    print ("Creando carpeta en: " + path)
    try:
        os.mkdir(path)
    except:
        print ("Err: No se pudo crear el directorio " +  path)
        exit(-1)

def identify_screen(img:Image)->bool:
    time.sleep(1)
    print ("identify_screen: " + str(img))
    intentos=0
    max_intentos = 10
    while (pa.locateOnScreen(img,confidence=cfg.scan['confidence']) == None and intentos <= max_intentos):
        print ("Warn: Imagen no encontrada. Reintentando #" + str(intentos))
        intentos +=1
        time.sleep(1)

    if (intentos >= max_intentos):
        print ("Err: Imagen no encontrada.")
        return False
    else:
        print ("Imagen encontrada")
        return True
    

moverA = pa.moveTo
obtener_posicion = pa.position
pauto=pa

def procesar_pantalla(img:Image, hacer_click:bool=True)->coords:
    if (not identify_screen(img)):
        exit(-1)
    else:
        zero = pa.locateOnScreen(img,confidence=cfg.scan['confidence'])
        #actual = pa.position()
        #destino =  math.sqrt((x2-x1)**2+(y2-y1)**2)
        #Se mueve a la zona detectada
        print ("Moviendo a imagen encontrada...")
        pa.moveTo(zero.left + zero.width/2, zero.top + zero.height/2,duration=3)
        #Entra en el icono
        if hacer_click:click()
        return coords((zero.left,zero.top))
    
def write_to_csv(data:list):
    with open (cfg.paths['csv'] + "test.csv",'a', newline='', encoding="utf-8") as file:
        wr = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
        wr.writerow(data)

def parse_profile()->dict:
    print ("Analizando perfil")

    #ID
    texto_temp = pytesseract.image_to_string(tmp_image_id, config=cfg.tesseract['cfg_only_numbers'])
    try:
        profile_id = int ( ''.join(filter(str.isdigit, texto_temp)))
    except:
        profile_id=0
    
    j.id= profile_id
    print ("Obtenido ID: " + str(profile_id))
    
    #Alianza
    texto_temp = pytesseract.image_to_string(tmp_image_alianza, config=cfg.tesseract['cfg_alphanumeric'])
    try:
        profile_alianza = texto_temp
        print ("Obtenido Alianza: " + str(profile_alianza))
    except:
        profile_alianza='ErrAlianza'
        print ("Err: No se ha obtenido la alianza")
    j.alianza=profile_alianza    

    #Poder Actual
    texto_temp = pytesseract.image_to_string(tmp_image_poderactual, config=tesseract_config_only_numbers)
    try:
        profile_poderactual = int ( ''.join(filter(str.isdigit, texto_temp)))
        print ("Obtenido Poder Actual: " + str(profile_poderactual))
    except:
        profile_poderactual = -1
        print ("Err: No se ha obtenido el poder actual")
    j.poderactual=profile_poderactual
    

    #Poder Mas Alto
    texto_temp = pytesseract.image_to_string(tmp_image_podermasalto, config=tesseract_config_only_numbers)
    try:
        profile_podermasalto = int ( ''.join(filter(str.isdigit, texto_temp)))
        print ("Obtenido Poder Mas Alto: " + str(profile_podermasalto))
    except:
        profile_podermasalto = -1
        print ("Err: No se ha podido obtener el poder mas alto")
    j.podermasalto=profile_podermasalto
    

    #Muertes
    texto_temp = pytesseract.image_to_string(tmp_image_muertos, config=tesseract_config_only_numbers)
    try:
        profile_muertos = int ( ''.join(filter(str.isdigit, texto_temp)))
        print ("Obtenido Muertos: " + str(profile_muertos))
    except:
        profile_muertos = -1
        print ("Err: No se ha podido obtener los muertos")
    j.muertos=profile_muertos
    

    #T4Kills
    texto_temp = pytesseract.image_to_string(tmp_image_t4kills, config=tesseract_config_only_numbers)
    try:
        profile_t4kills = int ( ''.join(filter(str.isdigit, texto_temp)))
        print ("Obtenido T4Kills: " + str(profile_t4kills))
    except:
        profile_t4kills = -1
        print ("Err: No se han podido obtener las T4Kills")
    j.t4kills = profile_t4kills
    
    
    #T5Kills
    texto_temp = pytesseract.image_to_string(tmp_image_t5kills, config=tesseract_config_only_numbers)
    try:
        profile_t5kills = int ( ''.join(filter(str.isdigit, texto_temp)))
        print ("Obtenido T5Kills: " + str(profile_t5kills))
    except:
        profile_t5kills = -1
        print ("Err: No se han podido obtener las T5Kills")
    j.t5kiils=profile_t5kills
    

    result = j.getJugador()

    write_to_csv(result)

    return result  
