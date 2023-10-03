import utils as u
import cfg as c
import os
from PIL import Image
import cv2 as cv
from jugador import jugador
from datetime import datetime
directorio_base = f"{c.SCANS_PATH}"

directorio_analisis = '20231003_214538_3131'
dir_in = f"{directorio_base}{directorio_analisis}/{c.SCREENSHOTS_PATH}"
kdname = directorio_analisis[16:20]
filename_csv = f"{directorio_base}{directorio_analisis}/{directorio_analisis}.csv"



profile_sufix = "_profile.png"
standing_sufix = "_standings.png"
more_info_sufix = "_more_info.png"
kp_sufix = "_kp.png"
name_sufix = "_name.txt"
timestamp_sufix = "_timestamp.txt"

##REGIONS
REGION_PROFILE_GOV_ID = (550,120,700,155)
REGION_PROFILE_ALLIANCE = (400,250,640,290)
REGION_PROFILE_POWER = (650,250,870,290)
REGION_PROFILE_KP = (880,250,1140,290)

REGION_MORE_INFO_POWER = (640,110,865,150)
REGION_MORE_INFO_POWERH = (800,230,1150,280)
REGION_MORE_INFO_DEATHS = (800,410,1150,460)
REGION_MORE_INFO_RSS_ASSIST = (800,630,1150,680)

REGION_KP_T4 = (651,370,900,405)
REGION_KP_T5 = (651,415,900,450)

def capture_region_from_file(img:Image, region)->Image:
    img_data = img.crop(region)
    return img_data


def get_numeric_data_from_image(img_path:str, region, prepare_image=True)->int:
    print (img_path)
    try:
        img = Image.open(img_path)
        if (prepare_image): 
            img2 = u.prepare_image(capture_region_from_file(img,region)) 
        else:
            img2= capture_region_from_file(img,region)
        #img2 = capture_region_from_file(img,region)
        return u.datos_numericos (img2)  
    except FileNotFoundError:
        return -1
      

def get_alphanumeric_data_from_image(img_profile_path:str, region)->str:
    try:
        img_profile = Image.open(img_profile_path)
        img2 = u.prepare_image(capture_region_from_file(img_profile,region))
        return u.datos_alfanumericos (img2)
    except FileNotFoundError:
        return "#error#"

def get_nombre_from_file (txt_file_path:str)->str:
    try:
        with open(txt_file_path,mode='r',encoding="utf-8") as f:
            name = f.read()
            return name
    except FileNotFoundError:
        return "InactivePlayer"

def get_timestamp_from_file (txt_file_path:str)->float:
    try:
        with open(txt_file_path,mode='r',encoding="utf-8") as f:
            data = f.read()
            return float(data)
    except FileNotFoundError:
        return datetime.timestamp(datetime.utcnow())


posicion_ini=1
posicion_final = 300



for posicion in range(posicion_ini,posicion_final+1):
    j = jugador()

    img_profile_path = f"{dir_in}/{kdname}_{posicion}{profile_sufix}" 
    img_more_info_path = f"{dir_in}/{kdname}_{posicion}{more_info_sufix}" 
    img_kp_path = f"{dir_in}/{kdname}_{posicion}{kp_sufix}" 
    txt_file_path = f"{dir_in}/{kdname}_{posicion}{name_sufix}" 
    txt_timestamp_path =f"{dir_in}/{kdname}_{posicion}{timestamp_sufix}" 

    j.kd = kdname
    j.pos = posicion
    j.id = get_numeric_data_from_image(img_profile_path, REGION_PROFILE_GOV_ID)
    j.nombre= get_nombre_from_file(txt_file_path)
    j.alianza = get_alphanumeric_data_from_image(img_profile_path, REGION_PROFILE_ALLIANCE)
    j.poderactual = get_numeric_data_from_image(img_profile_path, REGION_PROFILE_POWER, False)
    j.podermasalto = get_numeric_data_from_image(img_more_info_path, REGION_MORE_INFO_POWERH)
    j.kp = get_numeric_data_from_image(img_profile_path, REGION_PROFILE_KP, False)
    j.muertos=get_numeric_data_from_image(img_more_info_path, REGION_MORE_INFO_DEATHS)
    j.rss_assist = get_numeric_data_from_image(img_more_info_path, REGION_MORE_INFO_RSS_ASSIST)

    j.t4kills = get_numeric_data_from_image(img_kp_path, REGION_KP_T4)
    j.t5kills = get_numeric_data_from_image(img_kp_path, REGION_KP_T5)

    j.timestamp = get_timestamp_from_file(txt_timestamp_path)

    print (j)
    
    u.write_to_csv(data=j.getJugador(), fichero= filename_csv, header=c.CSV_HEADER)



#print (get_numeric_data_from_image('./reporte_in/test/3131_11_profile.png', REGION_PROFILE_POWER, False))