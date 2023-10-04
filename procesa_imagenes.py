import utils as u
import cfg as c
import os
from PIL import Image
import cv2 as cv
from jugador import jugador
from datetime import datetime

class procesa_imagenes():
    logger = u.getmylogger(__name__)
    #FILE SUFIX
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

    def __init__(self) -> None:
        pass

    def capture_region_from_file(self,img:Image, region)->Image:
        img_data = img.crop(region)
        return img_data
    
    def get_numeric_data_from_image(self,img_path:str, region, prepare_image=True)->int:
        print (img_path)
        try:
            img = Image.open(img_path)
            if (prepare_image): 
                img2 = u.prepare_image(self.capture_region_from_file(img,region)) 
            else:
                img2= self.capture_region_from_file(img,region)
            #img2 = capture_region_from_file(img,region)
            return u.datos_numericos (img2)  
        except FileNotFoundError:
            return -1
        
    def get_alphanumeric_data_from_image(self,img_profile_path:str, region)->str:
        try:
            img_profile = Image.open(img_profile_path)
            img2 = u.prepare_image(self.capture_region_from_file(img_profile,region))
            return u.datos_alfanumericos (img2)
        except FileNotFoundError:
            return "#error#"

    def get_nombre_from_file (self,txt_file_path:str)->str:
        try:
            with open(txt_file_path,mode='r',encoding="utf-8") as f:
                name = f.read()
                return name
        except FileNotFoundError:
            return "InactivePlayer"

    def get_timestamp_from_file (self,txt_file_path:str)->float:
        try:
            with open(txt_file_path,mode='r',encoding="utf-8") as f:
                data = f.read()
                return float(data)
        except FileNotFoundError:
            return datetime.timestamp(datetime.utcnow())

    def start (self, dir_in:str, dir_out:str='', inicio:int=1, final:int=300)->bool:
        try:
            kdname = dir_in[16:20]
            self.filename_csv = f"{c.SCANS_PATH}{dir_in}/{dir_in}.csv"
            screeshots_location = f"{c.SCANS_PATH}{dir_in}/{c.SCREENSHOTS_PATH}"

            for posicion in range(inicio,final+1):
                j = jugador()

                img_profile_path = f"{screeshots_location}/{kdname}_{posicion}{self.profile_sufix}" 
                img_more_info_path = f"{screeshots_location}/{kdname}_{posicion}{self.more_info_sufix}" 
                img_kp_path = f"{screeshots_location}/{kdname}_{posicion}{self.kp_sufix}" 
                txt_file_path = f"{screeshots_location}/{kdname}_{posicion}{self.name_sufix}" 
                txt_timestamp_path =f"{screeshots_location}/{kdname}_{posicion}{self.timestamp_sufix}" 

                j.kd = kdname
                j.pos = posicion
                j.id = self.get_numeric_data_from_image(img_profile_path, self.REGION_PROFILE_GOV_ID)
                j.nombre= self.get_nombre_from_file(txt_file_path)
                j.alianza = self.get_alphanumeric_data_from_image(img_profile_path, self.REGION_PROFILE_ALLIANCE)
                j.poderactual = self.get_numeric_data_from_image(img_profile_path, self.REGION_PROFILE_POWER)
                j.podermasalto = self.get_numeric_data_from_image(img_more_info_path, self.REGION_MORE_INFO_POWERH)
                j.kp = self.get_numeric_data_from_image(img_profile_path, self.REGION_PROFILE_KP)
                j.muertos=self.get_numeric_data_from_image(img_more_info_path, self.REGION_MORE_INFO_DEATHS)
                j.rss_assist = self.get_numeric_data_from_image(img_more_info_path, self.REGION_MORE_INFO_RSS_ASSIST)

                j.t4kills = self.get_numeric_data_from_image(img_kp_path, self.REGION_KP_T4)
                j.t5kills = self.get_numeric_data_from_image(img_kp_path, self.REGION_KP_T5)

                j.timestamp = self.get_timestamp_from_file(txt_timestamp_path)

                self.logger.debug(j)    
            
                u.write_to_csv(data=j.getJugador(), fichero= self.filename_csv, header=c.CSV_HEADER)
            return True
        except:
            return False
        
    def get_csv_path(self)->str:
        return self.filename_csv


