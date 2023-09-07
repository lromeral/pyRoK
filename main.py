import utils as u
import jugador as j
import cfg as c
import time
import pyperclip as pc
from datetime import datetime
from PIL import Image

class main():
    def __init__(self, inicio:int=0, final:int=300) -> None:
        #Datetime
        global time_of_creation
        time_of_creation = datetime.now()
        global filename_csv
        filename_csv = c.paths['csv'] + time_of_creation.strftime('%Y%m%d_%H%M%S') + '_data.csv'
        
        self.main(inicio,final)

    #Accede al cuadro del detalle de muertes en la pantalla de Mas Informacion
    def accede_estadisticas_asesinato(self):
        if u.identify_screen(c.screens['more_info']):
            print ("Moviendo a info_kp",0.4)
            u.moverA(c.posiciones['kills'],duration=0.5)
            u.click()
        else:
            self.salir("No se encuentra la pantalla de perfil del gobernador")

    ##Accede a pantalla de Mas Información
    def accede_mas_info(self):
        if u.identify_screen(c.screens['profile']):
            print ("Moviendo a info_kp",0.4)
            u.moverA(c.posiciones['mas_info'])
            u.click()
        else:
            self.salir("No se encuentra la pantalla de perfil del gobernador")

    #Captura los datos necesarios en Mas Informacion
    def captura_info (self):
        if (not u.identify_screen(c.screens['more_info'])): 
            self.salir("No se encuentra en la pantalla de Mas Informacion")
        else:
            #Captura de datos
            #### Poder Mas Alto (Numerico)
            jugador.podermasalto = self.get_dato_numerico(c.regions['powerH'])
            #### Muertos (Numerico)
            jugador.muertos = self.get_dato_numerico(c.regions['deaths'])
            #### Asistencia Recursos (Numerico)
            jugador.assist_rss = self.get_dato_numerico(c.regions['assist_rss'])
            #Salir

    #Captura los datos del Perfil del Gobernador
    def captura_profile (self):
        if (not u.identify_screen(c.screens['profile'])): 
            self.salir("No se encuentra la pantalla de perfil del gobernador")
        else:
            #Captura de datos en PERFIL
            #### Poder Kill Points (Numerico)
            jugador.kp = self.get_dato_numerico(c.regions['kp_profile'])
            #### Poder Actual (Numerico)
            jugador.poderactual = self.get_dato_numerico(c.regions['power'])
            ####Alianza
            jugador.alianza = self.get_dato_alfanumerico(c.regions['alliance'])
            #### ID
            jugador.id = self.get_dato_numerico(c.regions['id'])
    
    def captura_estadisticas_asesinato (self):
            ####t4kills
            jugador.t4kills = self.get_dato_numerico(c.regions['t4kills'])
            #### t5kills
            jugador.t5kills = self.get_dato_numerico(c.regions['t5kills'])

    #Cierra la pantalla de Perfil del Gobernador
    def cerrar_perfil(self):
        if u.identify_screen(c.screens['profile']):
            u.moverA(c.posiciones['cerrar_perfil'],duration=0.3)
            u.click()
        else:
            self.salir("No se encuentra la pantalla de perfil del gobernador")

    #Cierra la pantalla de Mas Información
    def cerrar_mas_info(self):
        if u.identify_screen(c.screens['more_info']):
            u.moverA(c.posiciones['cerrar_mas_info'],duration=0.2)
            u.click()
        else:
            self.salir("No se encuentra la pantalla Mas Informacion")

    def copiar_nombre_mas_info(self):
        if u.identify_screen(c.screens['more_info']):
            u.moverA(c.posiciones['copy_name_mas_info'],duration=0.2)
            u.click()
        else:
            self.salir("No se encuentra la pantalla Mas Informacion")

    def copiar_nombre_profile(self):
        if u.identify_screen(c.screens['profile']):
            u.moverA(c.posiciones['copy_name2'],duration=0.3)
            u.click()
        else:
            self.salir("No se encuentra la pantalla Mas Informacion")

    #Devuelve los datos obtenidos sobre la alizanza
    def datos_alfanumericos(self,img:Image)->str:
        datos = u.pytesseract.image_to_string(img).strip()
        return datos if len(datos) > 3 else "#error#"
    
    #Devuelve los datos obtenidos sobre la id de jugador
    def datos_numericos(self,img:Image)->int:
        datos =  (u.pytesseract.image_to_string(img,config=c.tesseract['cfg_only_numbers']).strip())
        return int(datos) if datos.isnumeric() else -1

    def get_dato_numerico(self, region)->int:
        intentos=0
        max_intentos = 10
        while True:
            captura = u.capturar_region(region=region)
            dato = self.datos_numericos(captura)
            intentos +=1
            if (dato != -1 or intentos > max_intentos): 
                return dato
            print ("Reintentando dato numerico: " + str(intentos))
            time.sleep(0.1)

    def get_dato_alfanumerico(self, region)->int:
        intentos=0
        max_intentos = 10
        while True:
            captura = u.capturar_region(region=region)
            dato = self.datos_alfanumericos(captura)
            intentos +=1
            if (dato != '' or intentos > max_intentos): 
                return dato
            print ("Reintentando dato alfanumerico: " + str(intentos))
            time.sleep(0.1)
    #Procesa el jugador en cuestion
    def procesa_jugador(self,num, posicion)->None:
        global jugador
        jugador = j.jugador(pos=num, timestamp=datetime.timestamp(datetime.now()))
        if (u.identify_screen(c.screens['kd_standings_power'])):
            print ("Procesando Perfil #" + str(num+1))
            # Mueve el raton a las coordenadas del primer jugador
            u.moverA(posicion, duration=0.5)
            u.click()
        else:
            self.salir("No se encuentra en la pantalla de clasificaciones poder individual")
        #Captura datos del perfil
        self.captura_profile()
        #Accede a Mas Información
        self.accede_mas_info()
        ##Captura datos de Mas Informacion
        self.captura_info()
        ## Detalle kills
        self.accede_estadisticas_asesinato()
        #Captura t4kills y t5kills
        self.captura_estadisticas_asesinato()
        #Copia el nombre
        self.copiar_nombre_mas_info()
        ###Vuelve al perfil del jugador
        self.cerrar_mas_info()

        ##Dentro del perfil accede a Mas informacion
        #time.sleep(2)
        jugador.nombre = pc.paste()
        ##Mas info kp
        self.cerrar_perfil()

    #Aborta el programa con mensaje en consola
    def salir (self, mensaje:str):
        print (mensaje)
        exit(-1)
    
    #Programa principal
    def main(self, inicio:int=0, final:int=300)->bool:
        # Check pantalla principal
        #print (c.icons['profile'])
        """if u.procesar_pantalla(c.icons['profile']):
            print ("Perfil encontrado")
        else:
            print ("Perfil no encontrado")
            exit(-1)
        # TODO: Check pantalla Perfil del Gobernador
        
        # Pantalla Clasificaciones
        if (u.procesar_pantalla(c.icons['standings'])):
            pass
        else:
            print ("Icono de Clasificaciones no encontrado")
            exit(-1)
        #Pantalla Poder Individual
        ''''
        if(u.procesar_pantalla(c.icons['power'])):
            pass
        else:
            print ("Icono de poder individual no encontrado")
            exit(-1)
        """
        for x in range(inicio,final):
            print ("Procesando jugadores")
            if (x<=3): posicion = c.scan['first_pos'][0],c.scan['first_pos'][1] + x * c.scan['standings_space']
            self.procesa_jugador(num=x + 1 , posicion=posicion)
            print (jugador)
            u.write_to_csv(data=jugador.getJugador(), fichero= filename_csv, header=c.csv_header)
        return True


if __name__=='__main__':
    time.sleep(5)
    comienzo = datetime.now()
    print (comienzo)
    main(final=300)
    
    final =datetime.now()
    print (final)
    print (f"Tiempo transcurrido: {final - comienzo}")