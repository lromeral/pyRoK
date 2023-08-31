#Tamaño de la ventana del juego: 1280x720
#Posicion de la ventana al inciar:


import pyautogui as pa
import cv2
import numpy as np
import json
import time
import pytesseract
from PIL import Image


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
     
    @property
    def width (self) -> float:
        return self.__cords[0]
    @property
    def height (self) -> float:
        return self.__cords[1]
    @property
    def center (self) -> tuple:
        return self.width/2, self.height/2

        
##ICONOS DE REFERENCIA
img_icon_profile_pic = 'images/icon_profile_pic.png'
img_icon_clasificaciones = 'images/icon_clasificaciones.png'
img_icon_clasificaciones_poder='images/icon_clasificaciones_poder.png'

img_icon_masinfo = 'images/icon_masinformacion.png'
img_icon_infokp = 'images/icon_infokp.png'
img_icon_cerrar_perfil = 'images/icon_cerrar_perfil.png'

#CAPTURAS DE EJEMPLO
img_profile_detail = 'images/profile_detail.png'
img_profile_detail_kp = 'images/profile_detail_kp.png'
img_kp_stats = 'images/kp_stats.png'

#DATOS CONFIG
espacio_entre_perfiles = 100

tesseract_path="C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


###ENCUENTRA EL ICONO DE PERFIL DE LA VENTANA PARA REFERENCIAR PUNTOS

time.sleep(1)

def locate_image(img)->coords:
    zero = pa.locateOnScreen(img,confidence=0.9)
    print (zero)
    if (zero is None):
        print (zero)
        return coords()
    else:
        #Se mueve a la zona detectada
        print ('mueve')
        pa.moveTo(zero.left + zero.width/2, zero.top + zero.height/2,duration=3)
        print ('fin mueve')
        #Entra en el icono
        time.sleep(0.5)
        pa.mouseDown()
        time.sleep(0.1)
        pa.mouseUp()
        time.sleep(0.6)
        return coords((zero.left,zero.top))


def busca_dato (texto:str,str_inicio:str,str_final:str)->str:
    inicio = texto.find(str_inicio)
    final = texto.find(str_final)
    return texto[inicio + len(str_inicio):final].strip().replace(' ','')

def parse_profile(profile:Image, profile_kp:Image)->json:
    texto_profile = pytesseract.image_to_string(Image.open(profile))
    texto_profile_kp = pytesseract.image_to_string(Image.open(profile_kp))
    print (texto_profile_kp)
    result = {
        "Nombre":busca_dato(texto_profile,'','Poder'),
        "Poder": busca_dato(texto_profile,'Poder:', 'Pu'),
        "PoderMasAlto": busca_dato(texto_profile,'Alto',"V"),
        "Muertes": busca_dato(texto_profile,'Muerto','Mom'),
        "T4Kills": 0,
        "T5Kills": 0
    }
    return json.dumps(result)    

def testing():
    print (locate_image(img_icon_clasificaciones_poder))
    #Se posiciona en el primero de la lista
    pa.moveRel(0,-230,4)
    time.sleep(1.2)
    #Almacena posicion incial
    pos_ini = pa.position()
    
    #Recorre los 6 perfiles de la pagina
    for x in range(1,6):
        #Click en el perfil
        pa.click()
        time.sleep(0.4)
        
        #Navega a Mas información
        print (locate_image(img_icon_masinfo))
        
        #captura de pantalla
        #pa.screenshot()
        
        #Navega a Detalles KP
        print (locate_image(img_icon_infokp))
        
        #captura de pantalla
        #pa.screenshot()

        #Navega a Cerrar
        print (locate_image(img_icon_cerrar_perfil))
        time.sleep(2)
        #Navega a Cerrar
        print (locate_image(img_icon_cerrar_perfil))

        #Mueve al siguiente
        pa.moveTo(pos_ini.x, pos_ini.y + espacio_entre_perfiles * x,5)
        time.sleep(1.2 + 0.1*x)     
        
    

"""     time.sleep(1.2)
    pa.click()
    time.sleep(0.2)
    print (locate_image(img_icon_masinfo))
    time.sleep(0.45)
    pa.click()
    time.sleep(1.2)
    print (locate_image(img_icon_infokp))
    time.sleep(0.88)
    pa.click() """

testing()

#result = locate_image(img_profile_pic)
#result = locate_image(img_clasificaciones)
#result = locate_image(img_clasificaciones_poder)

#resultado =  (parse_profile(img_profile_detail,img_profile_detail_kp))
#texto_profile_kp = pytesseract.image_to_string(Image.open(img_kp_stats))
#print (texto_profile_kp)
#print (resultado)

