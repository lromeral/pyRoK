from utils import utilesRoK
import jugador as j
import cfg as c
import time
import pyperclip as pc
import logging
from datetime import datetime
from PIL import Image
from mylogger import getmylogger


class main():
    def __init__(self, inicio:int=0, final:int=300) -> None:
        self.u = utilesRoK() 
        self.logger = getmylogger(__name__)
        global time_of_creation
        time_of_creation = datetime.now()
        global filename_csv
        filename_csv = c.paths['csv'] + time_of_creation.strftime('%Y%m%d_%H%M%S') + '_data.csv'
        
        self.main(inicio,final)

    #Accede al cuadro del detalle de muertes en la pantalla de Mas Informacion
    def accede_estadisticas_asesinato(self):
        self.logger.debug ("Accediendo estasticas de asesinato")
        if self.u.identify_screen(c.screens['more_info']):
            self.u.moverA(c.posiciones['kills'],duration=0.5)
            self.u.click()
        else:
            self.logger.error ("No se encuentra la pantalla de Mas Información")
            self.salir("No se encuentra la pantalla de Mas Información")

    ##Accede a pantalla de Mas Información
    def accede_mas_info(self):
        self.logger.debug (self.accede_mas_info.__name__)
        if self.u.identify_screen(c.screens['profile']):
            self.u.moverA(c.posiciones['mas_info'])
            self.u.click()
        else:
            self.logger.error ("No se encuentra la pantalla de perfil del gobernador")
            self.salir("No se encuentra la pantalla de perfil del gobernador")

    #Captura los datos necesarios en Mas Informacion
    def captura_info (self):
        self.logger.debug (self.captura_info.__name__)
        if (not self.u.identify_screen(c.screens['more_info'])):
            self.logger.error ("No se encuentra en la pantalla de Mas Información") 
            self.salir("No se encuentra en la pantalla de Mas Informacion")
        else:
            jugador.podermasalto = self.get_dato_numerico(c.regions['powerH'])
            jugador.muertos = self.get_dato_numerico(c.regions['deaths'])
            jugador.assist_rss = self.get_dato_numerico(c.regions['assist_rss'])

    #Captura los datos del Perfil del Gobernador
    def captura_profile (self):
        self.logger.debug (self.captura_profile.__name__)
        if (not self.u.identify_screen(c.screens['profile'])): 
            self.logger.error ("No se encuentra en la pantalla de Perfil del Gobernador") 
            self.salir("No se encuentra la pantalla de perfil del gobernador")
        else:
            jugador.kp = self.get_dato_numerico(c.regions['kp_profile'])
            jugador.poderactual = self.get_dato_numerico(c.regions['power'])
            jugador.alianza = self.get_dato_alfanumerico(c.regions['alliance'])
            jugador.id = self.get_dato_numerico(c.regions['id'])
    
    def captura_estadisticas_asesinato (self):
            self.logger.debug (self.captura_estadisticas_asesinato.__name__)
            jugador.t4kills = self.get_dato_numerico(c.regions['t4kills'])
            jugador.t5kills = self.get_dato_numerico(c.regions['t5kills'])

    #Cierra la pantalla de Perfil del Gobernador
    def cerrar_perfil(self):
        self.logger.debug (self.cerrar_perfil.__name__)
        if self.u.identify_screen(c.screens['profile']):
            self.u.moverA(c.posiciones['cerrar_perfil'],duration=0.3)
            self.u.click()
        else:
            self.logger.error ("No se encuentra en la pantalla de Perfil del Gobernador") 
            self.salir("No se encuentra la pantalla de perfil del gobernador")

    #Cierra la pantalla de Mas Información
    def cerrar_mas_info(self):
        self.logger.debug (self.cerrar_mas_info.__name__)
        if self.u.identify_screen(c.screens['more_info']):
            self.u.moverA(c.posiciones['cerrar_mas_info'],duration=0.2)
            self.u.click()
        else:
            self.logger.error ("No se encuentra en la pantalla de Mas Información") 
            self.salir("No se encuentra la pantalla Mas Informacion")

    def copiar_nombre_mas_info(self):
        self.logger.debug (self.copiar_nombre_mas_info.__name__)
        if self.u.identify_screen(c.screens['more_info']):
            self.u.moverA(c.posiciones['copy_name_mas_info'],duration=0.2)
            self.u.click()
        else:
            self.logger.error ("No se encuentra en la pantalla de Más Información")
            self.salir("No se encuentra la pantalla Mas Informacion")

    def copiar_nombre_profile(self):
        self.logger.debug (self.copiar_nombre_profile.__name__)
        if self.u.identify_screen(c.screens['profile']):
            self.u.moverA(c.posiciones['copy_name2'],duration=0.3)
            self.u.click()
        else:
            self.logger.error ("No se encuentra en la pantalla de Perfil del Gobernador")
            self.salir("No se encuentra la pantalla Perfil del Gobernador")

    #Devuelve los datos obtenidos sobre la alizanza
    def datos_alfanumericos(self,img:Image)->str:
        self.logger.debug (self.datos_alfanumericos.__name__)
        datos = self.u.pytesseract.image_to_string(img).strip()
        return datos if len(datos) > 3 else "#error#"
    
    #Devuelve los datos obtenidos sobre la id de jugador
    def datos_numericos(self,img:Image)->int:
        self.logger.debug (self.datos_numericos.__name__)
        datos =  (self.u.pytesseract.image_to_string(img,config=c.tesseract['cfg_only_numbers']).strip())
        return int(datos) if datos.isnumeric() else -1

    def get_dato_numerico(self, region)->int:
        self.logger.debug (self.get_dato_numerico.__name__)
        intentos=0
        max_intentos = 10
        while True:
            captura = self.u.capturar_region(region=region)
            dato = self.datos_numericos(captura)
            intentos +=1
            if (dato != -1 or intentos > max_intentos): 
                return dato
            self.logger.warning ("Dato numerico no encontrado. #" + str(intentos))
            print ("Reintentando dato numerico: " + str(intentos))
            time.sleep(0.1)

    def get_dato_alfanumerico(self, region)->str:
        self.logger.debug (self.get_dato_alfanumerico.__name__)
        intentos=0
        max_intentos = 10
        while True:
            captura = self.u.capturar_region(region=region)
            dato = self.datos_alfanumericos(captura)
            intentos +=1
            if (dato != '' or intentos > max_intentos): 
                return dato
            self.logger.warning ("Dato alfanumerico no encontrado. #" + str(intentos))
            print ("Reintentando dato alfanumerico: " + str(intentos))
            time.sleep(0.1)

    #Procesa el jugador en cuestion
    def procesa_jugador(self,num, posicion)->None:
        self.logger.debug (self.procesa_jugador.__name__)
        self.logger.info ("Procesando jugador #" + str(num))
        global jugador
        jugador = j.jugador(pos=num, timestamp=datetime.timestamp(datetime.now()))
        if (self.u.identify_screen(img=c.screens['kd_standings_power'])):
            self.u.moverA(posicion, duration=0.5)
            self.u.click()

        else:
            self.logger.error("No se encuentra en la pantalla de Clasificación Poder Individual")
            self.salir("No se encuentra en la pantalla de clasificaciones poder individual")
        self.captura_profile()
        self.accede_mas_info()
        self.captura_info()
        self.accede_estadisticas_asesinato()
        self.captura_estadisticas_asesinato()
        self.copiar_nombre_mas_info()
        self.cerrar_mas_info()
        self.logger.debug ("Pega el nombre")
        jugador.nombre = pc.paste()
        self.cerrar_perfil()

    #Aborta el programa con mensaje en consola
    def salir (self, mensaje:str):
        self.logger.debug (self.salir.__name__)
        #print (mensaje)
        exit(-1)
    
    #Programa principal
    def main(self, inicio:int=0, final:int=300)->bool:
        self.logger.debug (self.main.__name__)
        self.logger.info (f"Procesando jugadores desde {inicio} hasta {final}")
        for x in range(inicio,final):
            if (x<=3): posicion = c.scan['first_pos'][0],c.scan['first_pos'][1] + x * c.scan['standings_space']
            self.procesa_jugador(num=x + 1 , posicion=posicion)
            self.u.write_to_csv(data=jugador.getJugador(), fichero= filename_csv, header=c.csv_header)
        return True


if __name__=='__main__':
    time.sleep(5)
    comienzo = datetime.now()
    print (comienzo)
    main(final=300)
    final =datetime.now()
    print (final)
    print (f"Tiempo transcurrido: {final - comienzo}")