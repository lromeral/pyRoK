import jugador as j
import cfg as c
import utils as u
import time
import pyperclip as pc
from mylogger import getmylogger 
from datetime import datetime
from PIL import Image, ImageEnhance


class scan():
    def __init__(self, kdname:str='' ,inicio:int=1, final:int=300) -> None:
        self.kdname = kdname
        self.inicio = inicio
        self.final = final
        self.logger = getmylogger(__name__)
        self.time_of_creation = datetime.now()
        self.filename_csv = c.PATHS['CSV'] + kdname + "_" + self.time_of_creation.strftime('%Y%m%d_%H%M%S') + '_data.csv'        
        self.inactivo = False

    def process_standings(self,position:tuple):
        self.logger.debug (self.process_standings.__name__)
        self.logger.debug (f"Haciendo click en la posicion {position}")
        u.click_on_location(position)
        
    def process_profile(self, pos_in_standings:int):
        self.logger.debug (self.process_profile.__name__)
        self.logger.debug (f"Procesando posicion: {pos_in_standings}")
        self.jugador.pos = pos_in_standings
        self.jugador.timestamp = datetime.timestamp(datetime.utcnow())
        #captura_in = ImageEnhance.Contrast(u.capture_region(c.DATA_ID).convert('L'))
        #captura_out = captura_in.enhance(3)
        #captura_out.show()
        #input()
        #INACTIVO
        if (not u.check_screeen(c.REGION_WINDOW_GOV_PROFILE,c.TITLE_WINDOW_GOV_PROFILE)):
            self.logger.debug("Jugador Inactivo")
            self.jugador.setInactivo()
            self.inactivo = True
            return
        self.jugador.id =  u.datos_numericos(u.capture_region(c.DATA_ID,True))
        self.jugador.alianza =  u.datos_alfanumericos(u.capture_region(c.DATA_ALLIANCE, True))
        self.jugador.poderactual = u.datos_numericos(u.capture_region(c.DATA_POWER, True))
        self.jugador.kp = u.datos_numericos(u.capture_region(c.DATA_KP, True))

    def process_more_info (self):
        self.logger.debug (self.process_more_info.__name__)
        u.click_on_location(c.CLICK_MORE_INFO)
        self.jugador.podermasalto = u.datos_numericos(u.capture_region(c.DATA_POWERH))
        #print (u.datos_numericos(u.capture_region(c.DATA_POWERH)))
        #u.capture_region(c.DATA_POWERH).show()
        #input()
        self.jugador.muertos = u.datos_numericos(u.capture_region(c.DATA_DEATHS))
        self.jugador.rss_assist = u.datos_numericos(u.capture_region(c.DATA_RSS_ASSIST))
        u.click_on_location (c.CLICK_COPY_NAME)
        self.jugador.nombre = pc.paste()
        self._process_kp_stats()
        u.click_on_location(c.CLICK_CLOSE_MORE_INFO)

    def _process_kp_stats (self):
        self.logger.debug (self._process_kp_stats.__name__)
        u.click_on_location(c.CLICK_KILLS_STATS)
        time.sleep(0.3)
        self.jugador.t4kills=u.datos_numericos(u.capture_region(c.DATA_T4KILLS))
        self.jugador.t5kills=u.datos_numericos(u.capture_region(c.DATA_T5KILLS))
    def close_profile(self):
        u.click_on_location(c.CLICK_CLOSE_GOV_PROFILE)
        
    def process_player (self,num:int, classf_position:tuple):
        self.logger.debug (self.process_player.__name__)
        self.process_standings(classf_position)
        time.sleep(0.5)
        #get data from profile
        self.process_profile(num)
        #INACTIVO
        if self.inactivo: return
        #access more_info
        time.sleep(1)
        self.process_more_info()
        #get data from more info
        time.sleep(0.5)
        #get data from kill stats
        #close profile
        self.close_profile()

   
    #Programa principal
    def start(self)->bool:
        self.logger.debug (self.start.__name__)
        self.logger.info (f"Procesando jugadores desde {self.inicio} hasta {self.final}")
        posicion_anterior=c.STANDING_POS[0]
        for x in range(self.inicio,self.final):
            self.jugador = j.jugador (kd=self.kdname)
            print (f"Posicion antes: {posicion_anterior}")
            if self.inactivo:
                indice_anterior = c.STANDING_POS.index(posicion_anterior)
                print (f"Indice anterior: {indice_anterior}")
                posicion_siguiente = c.STANDING_POS[indice_anterior + 1] if indice_anterior <=6 else exit(-1)
                self.inactivo =False
            else:
                posicion_siguiente = c.STANDING_POS[x] if x <=3 else c.STANDING_POS[4]
            print (f"Posicion despues: {posicion_siguiente}")
            self.process_player(num=x , classf_position=posicion_siguiente)
            self.logger.debug (self.jugador)
            u.write_to_csv(data=self.jugador.getJugador(), fichero= self.filename_csv, header=c.CSV_HEADER)
            posicion_anterior = posicion_siguiente
        return True

