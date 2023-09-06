#Tamaño de la ventana del juego: 1280x720
#Posicion de la ventana al inciar:



import time
import os
import pandas as pd
import pyperclip as pc

from classes.jugador import jugador

from datetime import datetime
from classes.cfg import *
from classes.utils import coords

###ENCUENTRA EL ICONO DE PERFIL DE LA VENTANA PARA REFERENCIAR PUNTOS

time.sleep(5)

def testing():
    #Nuevo jugador
    global j
    j = jugador()
    
    locate_image(img_icon_clasificaciones_poder)
    #Se posiciona en el primero de la lista
    pa.moveRel(0,-230,1.5)
    #Almacena posicion incial
    pos_ini = pa.position()
    
    #Crea el directorio para los screenshots 
    #Formato ddMMYY_HHMMSS
    dt_string = datetime.now().strftime("%Y%m%d_%H%M%S")
    actual_screenshot_path = os.path.join(conf_screenshots_path,dt_string)
    
    print ("Preparabdo carpeta para screenshots")
    crearCarpeta(actual_screenshot_path)

    print ("Procesando jugadores....")
    #Recorre los 6 perfiles de la pagina
    for x in range(conf_scan_ini,conf_scan_fin):
        print ("Procesando Jugador Numero: " + str(x))
        #Click en el perfil
        click()

        #Captura Perfil
        dt_string = datetime.now().strftime("%Y%m%d_%H%M%S")
        img_name = actual_screenshot_path + "\\" + str(x) + "_0_Perfil_"+dt_string + ".png"
        
        #Captura para parsear datos id
        global tmp_image_id
        tmp_image_id = ImageGrab.grab(bbox=region_id)
        
        #Captura para parsear datos Nombre
        global tmp_image_nombre
        tmp_image_nombre = ImageGrab.grab(bbox=region_nombre)

        #Captura para parsear datos Alianza
        global tmp_image_alianza
        tmp_image_alianza = ImageGrab.grab(bbox=region_alianza)


        print ("Capturando perfil #" + str(x))
        screenshot(img_name)
        
        print ("Navega Mas info")
        #Navega a Mas información
        locate_image(img_icon_masinfo)
        
        #captura de pantalla Mas info
        dt_string = datetime.now().strftime("%Y%m%d_%H%M%S")
        img_name = actual_screenshot_path + "\\" + str(x) +"_1_Mas_Info_"+dt_string + ".png"
        print ("Capturando perfil #" + str(x))
        screenshot(img_name)

        print ("Clipboard Name: " + pc.paste())

        #Captura Poder Actual
        global tmp_image_poderactual
        tmp_image_poderactual = ImageGrab.grab(bbox=region_poderactual)

        #Captura de Poder Mas Alto
        global tmp_image_podermasalto
        tmp_image_podermasalto = ImageGrab.grab(bbox=region_poder_mas_alto)
        
        #Captura de Muertos
        global tmp_image_muertos
        tmp_image_muertos = ImageGrab.grab(bbox=region_muerto)

        #Busca el icono de copiar el nombre
        locate_image(img_icon_copy_name)
        j.nombre=pc.paste()


        #Navega a Detalles KP
        print ("Navega detalles kp")
        locate_image(img_icon_infokp)
        
        #captura de pantalla
        dt_string = datetime.now().strftime("%Y%m%d_%H%M%S")
        img_name= actual_screenshot_path +  "\\" + str(x)  + "_2_Mas_Info_KP_"+ dt_string + ".png"
        print ("Capturando Detalles KP #" + str(x))
        screenshot(img_name)

        #Captura de t4kills
        global tmp_image_t4kills
        tmp_image_t4kills = ImageGrab.grab(bbox=region_t4kills)

        #Captura de t5kills
        global tmp_image_t5kills
        tmp_image_t5kills = ImageGrab.grab(bbox=region_t5kills)
        

        #Procesa los datos obtenidos
        print ("Parsea datos obtenidos")
        print (parse_profile())


        if (identify_screen(img_screen_mas_informacion)):
            #Navega a Cerrar
            print ("Navega a cerrar detalles perfil")
            locate_image(img_icon_cerrar_perfil)
        else:
            print ("Cerrar detalles perfil no encontrado")

        if (identify_screen(img_screen_perfil_gob)):
            #Navega a Cerrar
            print ("Navega a cerrar perfil gobernador")
            locate_image(img_icon_cerrar_perfil)
        else:
            print ("Cerrar perfil gobernador no encontrado")

        #Mueve al siguiente
        if (identify_screen(img_screen_clasificacion_poder)):
            if (x < 4):
                print ("Moviendo al siguiente jugador < 4")
                pa.moveTo(pos_ini.x, pos_ini.y + espacio_entre_perfiles * x,5)
                posicion =pa.position()
            else:
                print ("Moviendo al siguiente jugador >4")
                pa.moveTo(posicion, duration=3)
        else:
            print ("Err: No está en la ventana de clasificaciones")
            exit(-1) 

#
testing()