#Tamaño de la ventana del juego: 1280x720
#Posicion de la ventana al inciar:


import pyautogui as pa
import cv2
import numpy as np
import json
import time


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

        
##IMAGENES DE REFERENCIA

img_profile_pic = 'images/zeropoint.png'


###ENCUENTRA EL ICONO DE PERFIL DE LA VENTANA PARA REFERENCIAR PUNTOS

time.sleep(5)

def locate_profile()->coords:
    #img = pa.screenshot()
    zero = pa.locateOnScreen(img_profile_pic,confidence=0.9)
    print (zero)
    if (zero is None):
        print (zero)
        return coords()
    else:
        return coords((zero.left,zero.top))
    
screenSize = coords(pa.size())

profile_coords = locate_profile()
print (profile_coords)



if profile_coords != coords():
    pa.moveTo(profile_coords.width, profile_coords.height,duration=3)
    pa.mouseDown()
    time.sleep(0.5)
    pa.mouseUp()
    #pa.click(clicks=2, duration=1)

print (pa.position())