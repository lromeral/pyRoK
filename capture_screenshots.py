import jugador as j
import cfg as c
import utils as u
import pyperclip as pc
from mylogger import getmylogger 
from datetime import datetime
import os
import time
import utils as u

class captura_screenshots():
    def __init__(self, kdname:str='' ,inicio:int=1, final:int=300) -> None:
        self.inicio = inicio
        self.final = final
        self.kdname = kdname
        self.logger = getmylogger(__name__)
        self.inactivo = False
        self.image_location = datetime.now().strftime('%Y%m%d_%H%M%S') + "_" + str(self.kdname) 
        self.kd_scan_folder = c.SCANS_PATH + "/"  + self.image_location 
        self.screenshot_scan_folder = self.kd_scan_folder +"/" + c.SCREENSHOTS_PATH

    def get_scan_folder(self)->str:
        return self.image_location

    def process_standings(self,position:tuple, num:int):            
        self.logger.debug (self.process_standings.__name__)
        self.logger.debug (f"Haciendo click en la posicion {position}")
        if (not u.check_screeen(c.REGION_WINDOW_POWER_STANDINGS,c.TITLE_WINDOW_POWER_STANDINGS)): u.salir ("No se encuentra la ventana clasificaciones generales")
        nombre_archivo = f"{self.kdname}_{num}_standings.png"
        self.captura_pantalla(c.SCREENSHOT_STANDINGS,nombre_archivo)
        u.click_on_location(position)
        
    def process_profile(self, pos_in_standings:int):
        self.logger.debug (self.process_profile.__name__)
        self.logger.debug (f"process_profile: {pos_in_standings}")
        nombre_archivo = f"{self.screenshot_scan_folder }/{self.kdname}_{pos_in_standings}_timestamp.txt"
        with open(nombre_archivo, 'w',encoding="utf-8") as f:
            f.write(str(datetime.timestamp(datetime.utcnow())))
        self.jugador.pos = pos_in_standings
        self.jugador.timestamp = datetime.timestamp(datetime.utcnow())
        #INACTIVO
        if (not u.check_screeen(c.REGION_WINDOW_GOV_PROFILE,c.TITLE_WINDOW_GOV_PROFILE)):
            self.logger.debug("Jugador Inactivo")
            self.jugador.setInactivo()
            self.inactivo = True
            return
        #Captura la pantalla de perfil
        if (not u.check_screeen(c.REGION_WINDOW_GOV_PROFILE,c.TITLE_WINDOW_GOV_PROFILE)): u.salir ("No se encuentra la ventana perfil del gobernador")
        nombre_archivo = f"{self.kdname}_{pos_in_standings}_profile.png"
        self.captura_pantalla(c.SCREENSHOT_GOV_PROFILE,nombre_archivo)

    def process_more_info (self, pos_in_standings):
        self.logger.debug (self.process_more_info.__name__)
        u.click_on_location(c.CLICK_MORE_INFO)
        nombre_archivo = f"{self.kdname}_{pos_in_standings}_more_info.png"
        if (not u.check_screeen(c.REGION_WINDOW_MORE_INFO,c.TITLE_WINDOW_MORE_INFO)): u.salir ("No se encuentra la ventana mas infomacion")
        self.captura_pantalla(c.SCREENSHOT_MORE_INFO, nombre_archivo)
        u.click_on_location (c.CLICK_COPY_NAME)
        self.jugador.nombre = pc.paste()
        nombre_archivo = f"{self.screenshot_scan_folder }/{self.kdname}_{pos_in_standings}_name.txt"
        with open(nombre_archivo, 'w',encoding="utf-8") as f:
            f.write(self.jugador.nombre)
        self._process_kp_stats(pos_in_standings)
        u.click_on_location(c.CLICK_CLOSE_MORE_INFO)

    def _process_kp_stats (self, pos_in_standings:int):
        self.logger.debug (self._process_kp_stats.__name__)
        if (not u.check_screeen(c.REGION_WINDOW_MORE_INFO,c.TITLE_WINDOW_MORE_INFO)): u.salir ("No se encuentra la ventana mas infomacion procesando kp details")
        u.click_on_location(c.CLICK_KILLS_STATS)
        nombre_archivo = f"{self.kdname}_{pos_in_standings}_kp.png"
        self.captura_pantalla(c.SCREENSHOT_MORE_INFO ,nombre_archivo)

        
    def process_player (self,num:int, classf_position:tuple):
        self.logger.debug (self.process_player.__name__)
        self.logger.info(f"Procesando jugador{num}")
        self.process_standings(classf_position,num)
        self.process_profile(num)
        #INACTIVO
        if self.inactivo: return
        self.process_more_info(num)
        self.close_profile()

    def captura_pantalla (self,region,filename):
        time.sleep(1)
        self.logger.debug (self.captura_pantalla.__name__)
        self.logger.debug (f"Captura:{filename}")
        time.sleep(0.5)
        u.capture_region(region).save(self.screenshot_scan_folder + filename)

    def start(self)->bool:
        try:
            #Crea directorios si no existen
            if (not os.path.isdir(self.screenshot_scan_folder)): os.makedirs (self.screenshot_scan_folder)
            self.logger.debug (self.start.__name__)
            self.logger.info (f"Procesando jugadores desde {self.inicio} hasta {self.final}")
            posicion_anterior=c.STANDING_POS[0]
            for x in range(self.inicio,self.final):
                self.jugador = j.jugador (kd=self.kdname)
                if self.inactivo:
                    indice_anterior = c.STANDING_POS.index(posicion_anterior)
                    posicion_siguiente = c.STANDING_POS[indice_anterior + 1] if indice_anterior <=6 else u.salir ("Error de indice de jugador al procesar inactivos")
                    self.inactivo =False
                else:
                    posicion_siguiente = c.STANDING_POS[x] if x <=3 else c.STANDING_POS[4]
                self.process_player(num=x , classf_position=posicion_siguiente)
                posicion_anterior = posicion_siguiente
            return True
        except:
            return False
    