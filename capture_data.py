import cv2
import numpy as np
import pytesseract
import utils as u
import cfg
import os
import jugador as j
import time
import pyperclip as pc
from mylogger import getmylogger
from datetime import datetime
from custom_errors import WindowNotFound

class capture_data:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def __init__(self, kdname:str='' ,inicio:int=1, final:int=300) -> None:
        self.inicio = inicio
        self.final = final
        self.kdname = kdname
        self.logger = getmylogger(__name__)
        self.inactivo = False
        self.image_location = datetime.now().strftime('%Y%m%d_%H%M%S') + "_" + str(self.kdname) 
        self.kd_scan_folder = cfg.SCANS_PATH + "/"  + self.image_location 
        self.screenshot_scan_folder = self.kd_scan_folder +"/" + cfg.SCREENSHOTS_PATH

    def get_scan_folder(self)->str:
        return self.image_location

    def get_location_position(self,position:int)->tuple:
        assert (u.check_screeen(cfg.REGION_WINDOW_POWER_STANDINGS,cfg.TITLE_WINDOW_POWER_STANDINGS)), "get_location_position No se encuentra pantalla"
        #TODO: INVESTIGAR COMO BUSCAR LOS TRES PRIMEROS
        if position < 4:
            return cfg.STANDING_POS[position]
        
        #left_x, top_y, right_x, bottom_y
        img_pil = u.capture_region(cfg.SCREENSHOT_STANDINGS,False)
        img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        y=cfg.REGION_CROP_STANDINGS[1]
        x=cfg.REGION_CROP_STANDINGS[0]
        h=cfg.REGION_CROP_STANDINGS[3] - cfg.REGION_CROP_STANDINGS[1]
        w=cfg.REGION_CROP_STANDINGS[2] - cfg.REGION_CROP_STANDINGS[0]

        #image = cv2.imread(img)
        crop = img[y:y+h, x:x+w]
        #gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        #invert = 255 - gray
        #sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        #sharpen = cv2.filter2D(invert, -1, sharpen_kernel)
        #thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        #thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_OTSU)[1]
        

        #MASK el amarillo del numero de la clasificacion
        hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
        # define range of yellow color in HSV
        #(46,100,100) en rango (0-360, 0-100, 0-100) y opencv trabaja en (0-179, 0-255,0-255)
        lower_yellow = np.array([20, 245, 245])
        upper_yellow = np.array([25, 255, 255])
        # Create a mask. Threshold the HSV image to get only yellow colors
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        # Bitwise-AND mask and original image
        result = cv2.bitwise_and(crop,crop, mask= mask)
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        invert = 255 - gray

        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(invert, -1, sharpen_kernel)
        #thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        imagen_analizada = invert
        #cv2.imshow("result",result)
        #cv2.imshow("gray",gray)
        #cv2.imshow("sharpen",sharpen)
        #cv2.imshow("invert",invert)
        #cv2.imshow("imagen analizada",imagen_analizada)
        #cv2.waitKey(0)

        d = pytesseract.image_to_data(imagen_analizada, output_type=pytesseract.Output.DICT,config=" --psm 6 -c tessedit_char_whitelist=0123456789")
        #d = pytesseract.image_to_data(imagen_analizada, output_type=pytesseract.Output.DICT,config=" --psm 6 --oem 1 digits")
        print (d)    
        texts = d['text']
        lefts = d['left']
        tops = d ['top'] 

        texts2 = list([])
        tops2 = list([])
        lefts2 = list([])

        #Crea listas solo con numeros validos
        for i in range(0,len(texts)):
            print (f"i:{i}")
            if (texts[i].isdigit()):
                texts2.append(int(texts[i]))
                tops2.append(tops[i])
                lefts2.append(lefts[i])

        for i in range(0,len(texts2)):
            print (f"i:{i}")
            print(f"Buscando: {position} contra {texts2[i]}")
            if (texts2[i]==position):
                print (lefts2[i])
                print (tops2[i])
                left_screenshot =  cfg.SCREENSHOT_STANDINGS[0] + cfg.REGION_CROP_STANDINGS[0] + lefts2[i]
                top_screenshot= cfg.SCREENSHOT_STANDINGS[1] + cfg.REGION_CROP_STANDINGS[1] + tops2[i]
                return (left_screenshot, top_screenshot)

        #Direccion en la que buscar
        primero = texts2[0]
        ultimo = texts2[-1]
        direccion = False

        if ultimo < position:
            #Esta por debajo
            direccion = True
        elif primero > direccion:
            direccion = False
        DESPLAZAMIENTO_SCROLL = 110
        u.scroll(DESPLAZAMIENTO_SCROLL,direccion)
        print ("despues del scroll")
        #Vuelta a buscar
        return self.get_location_position(position)

    def process_player (self,num:int):
        self.logger.debug (self.process_player.__name__)
        self.logger.info(f"Procesando jugador{num}")
        if (self.process_standings(num)):
            self.process_profile(num)
            self.process_more_info(num)
            self.close_profile()

    ################# 01 STANDINGS ####################
    def process_standings(self,num:int)->bool:            
        self.logger.debug (self.process_standings.__name__)
        if (not u.check_screeen(cfg.REGION_WINDOW_POWER_STANDINGS,cfg.TITLE_WINDOW_POWER_STANDINGS)):
            u.salir ( "process_standings: No se encuentra pantalla de clasificaciones generales")
        position = self.get_location_position(num)
        nombre_archivo = f"{self.screenshot_scan_folder}/{self.kdname}_{num}_standings.png"
        u.captura_pantalla(cfg.SCREENSHOT_STANDINGS,nombre_archivo)
        u.click_on_location(position)
        #Gestion de Inactivos
        return (u.check_screeen(cfg.REGION_WINDOW_GOV_PROFILE,cfg.TITLE_WINDOW_GOV_PROFILE))
            

    ################# 02 PROFILE ####################  
    def process_profile(self, pos_in_standings:int):
        self.logger.debug (self.process_profile.__name__)
        self.logger.debug (f"process_profile: {pos_in_standings}")
        if (not u.check_screeen(cfg.REGION_WINDOW_GOV_PROFILE,cfg.TITLE_WINDOW_GOV_PROFILE)):
            u.salir("process_profile: No se encuentra la ventana perfil del gobernador")
        nombre_archivo = f"{self.screenshot_scan_folder }/{self.kdname}_{pos_in_standings}_timestamp.txt"
        with open(nombre_archivo, 'w',encoding="utf-8") as f:
            f.write(str(datetime.timestamp(datetime.utcnow())))
        self.jugador.pos = pos_in_standings
        self.jugador.timestamp = datetime.timestamp(datetime.utcnow())
        #Captura la pantalla de perfil
        nombre_archivo = f"{self.screenshot_scan_folder}/{self.kdname}_{pos_in_standings}_profile.png"
        u.captura_pantalla(cfg.SCREENSHOT_GOV_PROFILE,nombre_archivo)


    def close_profile(self):
        self.logger.debug (self.close_profile.__name__)
        if (not u.check_screeen(cfg.REGION_WINDOW_GOV_PROFILE,cfg.TITLE_WINDOW_GOV_PROFILE)): 
            raise WindowNotFound("No se encuentra la ventana perfil del gobernador")
        u.click_on_location(cfg.CLICK_CLOSE_GOV_PROFILE)
        time.sleep(0.5)
    
    ################# 03 MORE INFO ####################  
    def process_more_info (self, pos_in_standings):
        self.logger.debug (self.process_more_info.__name__)
        u.click_on_location(cfg.CLICK_MORE_INFO)
        nombre_archivo = f"{self.screenshot_scan_folder}/{self.kdname}_{pos_in_standings}_more_info.png"
        if (not u.check_screeen(cfg.REGION_WINDOW_MORE_INFO,cfg.TITLE_WINDOW_MORE_INFO)):
            u.salir ("process_more_info: No se encuentra la ventana mas informacion")
        u.captura_pantalla(cfg.SCREENSHOT_MORE_INFO, nombre_archivo)
        u.click_on_location (cfg.CLICK_COPY_NAME)
        self.jugador.nombre = pc.paste()
        nombre_archivo = f"{self.screenshot_scan_folder }/{self.kdname}_{pos_in_standings}_name.txt"
        with open(nombre_archivo, 'w',encoding="utf-8") as f:
            f.write(self.jugador.nombre)
        self._process_kp_stats(pos_in_standings)
        u.click_on_location(cfg.CLICK_CLOSE_MORE_INFO)

    def _process_kp_stats (self, pos_in_standings:int):
        self.logger.debug (self._process_kp_stats.__name__)
        if (not u.check_screeen(cfg.REGION_WINDOW_MORE_INFO,cfg.TITLE_WINDOW_MORE_INFO)): 
            raise WindowNotFound("_process_kp_stats: No se encuentra la ventana mas informacion")
        u.click_on_location(cfg.CLICK_KILLS_STATS)
        nombre_archivo = f"{self.screenshot_scan_folder}/{self.kdname}_{pos_in_standings}_kp.png"
        u.captura_pantalla(cfg.SCREENSHOT_MORE_INFO ,nombre_archivo)



    ################# START CAPTURING ####################  
    def start(self)->bool:
        try:
            #Crea directorios si no existen
            if (not os.path.isdir(self.screenshot_scan_folder)): os.makedirs (self.screenshot_scan_folder)
            self.logger.debug (self.start.__name__)
            self.logger.info (f"Procesando jugadores desde {self.inicio} hasta {self.final}")
            for x in range(self.inicio,self.final):
                self.jugador = j.jugador (kd=self.kdname)
                self.process_player(x)
            return True
        except Exception as e:
            print (f"Excepcion en capture:  {e}")
            return False



# c = capture_data('3131',1,300)
# c.start()