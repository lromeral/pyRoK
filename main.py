import jugador as j
import cfg as c
import time
import pyperclip as pc
import utils as u
from datetime import datetime
from PIL import Image
from mylogger import getmylogger



class main():

    def __init__(self, kdname:str='' ,inicio:int=1, final:int=300) -> None:
        self.jugador = j.jugador(kd=kdname)
        self.kdname = kdname
        self.inicio = inicio
        self.final = final
        self.logger = getmylogger(__name__)
        self.time_of_creation = datetime.now()
        self.filename_csv = c.paths['csv'] + kdname + "_" + self.time_of_creation.strftime('%Y%m%d_%H%M%S') + '_data.csv'
        
        self.inactivo = False

    def accede_perfil_clasificaciones(self,pos:int, duration:float=0.5)->bool:
        u.moverA(c.pos_clasificacion[pos],duration=duration)
        u.click()
        return True

    #Accede al cuadro del detalle de muertes en la pantalla de Mas Informacion
    def accede_estadisticas_asesinato(self):
        self.logger.debug ("Accediendo estasticas de asesinato")
        if u.is_screen(c.regions['title_mas_informacion'], c.titulos['mas_info'], self.jugador):
            u.moverA(c.posiciones['kills'],duration=0.1)
            u.click()
        else:
            self.logger.error ("No se encuentra la pantalla de Mas Información")
            u.salir("No se encuentra la pantalla de Mas Información")

    ##Accede a pantalla de Mas Información
    def accede_mas_info(self):
        self.logger.debug (self.accede_mas_info.__name__)
        if u.is_screen(c.regions['title_gobernador'], c.titulos['perfil_gob'], self.jugador):
            u.moverA(c.posiciones['mas_info'])
            u.click()
        else:
            self.logger.error ("No se encuentra la pantalla de perfil del gobernador")
            u.salir("No se encuentra la pantalla de perfil del gobernador")

    #Captura los datos necesarios en Mas Informacion
    def captura_info (self):
        self.logger.debug (self.captura_info.__name__)
        if (not u.is_screen(c.regions['title_mas_informacion'], c.titulos['mas_info'], self.jugador)):
            self.logger.error ("No se encuentra en la pantalla de Mas Información") 
            u.salir("No se encuentra en la pantalla de Mas Informacion")
        else:
            self.jugador.podermasalto = u.get_dato_numerico(c.regions['powerH'],3,self.jugador,True)
            self.jugador.muertos = u.get_dato_numerico(c.regions['deaths'],3,self.jugador,True)
            self.jugador.assist_rss = u.get_dato_numerico(c.regions['assist_rss'],3,self.jugador,True)

    #Captura los datos del Perfil del Gobernador
    def captura_profile (self):
        self.logger.debug (self.captura_profile.__name__)
        if (not u.is_screen(c.regions['title_gobernador'], c.titulos['perfil_gob'],self.jugador)): 
            self.logger.error ("No se encuentra en la pantalla de Perfil del Gobernador") 
            u.salir("No se encuentra la pantalla de perfil del gobernador")
        else:
            self.jugador.kp = u.get_dato_numerico(c.regions['kp_profile'],3,self.jugador,True)
            self.jugador.poderactual = u.get_dato_numerico(c.regions['power'],3,self.jugador,True)
            self.jugador.alianza = u.get_dato_alfanumerico(c.regions['alliance'],3,self.jugador,True)
            self.jugador.id = u.get_dato_numerico(c.regions['id'],3,self.jugador,True)
    
    def captura_estadisticas_asesinato (self):
            time.sleep(0.5)
            self.logger.debug (self.captura_estadisticas_asesinato.__name__)
            self.jugador.t4kills = u.get_dato_numerico(c.regions['t4kills'],3,self.jugador,True)
            self.jugador.t5kills = u.get_dato_numerico(c.regions['t5kills'],3,self.jugador,True)

    #Cierra la pantalla de Perfil del Gobernador
    def cerrar_perfil(self):
        self.logger.debug (self.cerrar_perfil.__name__)
        if u.is_screen(c.regions['title_gobernador'], c.titulos['perfil_gob'],self.jugador):
            u.moverA(c.posiciones['cerrar_perfil'],duration=0.1)
            u.click()
        else:
            self.logger.error ("No se encuentra en la pantalla de Perfil del Gobernador") 
            u.salir("No se encuentra la pantalla de perfil del gobernador")

    #Cierra la pantalla de Mas Información
    def cerrar_mas_info(self):
        self.logger.debug (self.cerrar_mas_info.__name__)
        if u.is_screen(c.regions['title_mas_informacion'], c.titulos['mas_info'], self.jugador):
            u.moverA(c.posiciones['cerrar_mas_info'],duration=0.2)
            u.click()
        else:
            self.logger.error ("No se encuentra en la pantalla de Mas Información") 
            u.salir("No se encuentra la pantalla Mas Informacion")

    def copiar_nombre_mas_info(self):
        self.logger.debug (self.copiar_nombre_mas_info.__name__)
        if u.is_screen(c.regions['title_mas_informacion'], c.titulos['mas_info'], self.jugador):
            u.moverA(c.posiciones['copy_name_mas_info'],duration=0.1)
            u.click()
        else:
            self.logger.error ("No se encuentra en la pantalla de Más Información")
            u.salir("No se encuentra la pantalla Mas Informacion")

    def copiar_nombre_profile(self):
        self.logger.debug (self.copiar_nombre_profile.__name__)
        if u.is_screen(c.screens['profile'], c.titulos['perfil_gob'], self.jugador):
            u.moverA(c.posiciones['copy_name2'],duration=0.1)
            u.click()
        else:
            self.logger.error ("No se encuentra en la pantalla de Perfil del Gobernador")
            u.salir("No se encuentra la pantalla Perfil del Gobernador")

    #Procesa el jugador en cuestion
    def procesa_jugador(self,num, posicion)->None:
        self.logger.debug (self.procesa_jugador.__name__)
        self.logger.info ("Procesando jugador #" + str(num))
        self.jugador.pos = num
        self.jugador.timestamp = datetime.timestamp(datetime.now())
        
        if (u.is_screen(region=c.regions['title_clasificacion_poder'], titulo_ventana=c.titulos['classificacion'], datos=self.jugador)):
            self.accede_perfil_clasificaciones(pos=posicion, duration=0.1)
            #Esquiva inactivos
            if (not u.is_screen(c.regions['title_gobernador'], c.titulos['perfil_gob'],self.jugador)): 
                self.logger.warning ("Jugador Inactivo")
                self.jugador.setInactivo()
                #self.accede_perfil_clasificaciones(pos=posicion+1, duration=0.5)
                self.inactivo = True
                return
        else:
            self.logger.error("No se encuentra en la pantalla de Clasificación Poder Individual")
            u.salir("No se encuentra en la pantalla de clasificaciones poder individual")
        self.captura_profile()
        self.accede_mas_info()
        self.captura_info()
        self.accede_estadisticas_asesinato()
        self.captura_estadisticas_asesinato()
        self.copiar_nombre_mas_info()
        self.cerrar_mas_info()
        self.logger.debug ("Pega el nombre")
        self.jugador.nombre = pc.paste()
        self.cerrar_perfil()
        self.inactivo = False

    #Programa principal
    def start(self)->bool:
        self.logger.debug (self.start.__name__)
        self.logger.info (f"Procesando jugadores desde {self.inicio} hasta {self.final}")
        for x in range(self.inicio,self.final):
            posicion = x if x <=3 else 4
            if self.inactivo: 
                self.logger.warning ("Saltando posicion por jugador inactivo")
                posicion = 5
            self.procesa_jugador(num=x , posicion=posicion)
            u.write_to_csv(data=self.jugador.getJugador(), fichero= self.filename_csv, header=c.csv_header)
        return True


if __name__=='__main__':
    
    kd = input("Nombre del Reino: ")
    i = int (input("Inicio: "))
    f = int(input('Final: ')) +1
    time.sleep(3)
    m = main(kdname=kd, inicio=i ,final=f)
    comienzo = datetime.utcnow()
    m.logger.info (comienzo)
    
    m.start()

    #print (u.get_dato_numerico(c.regions['t4kills']))
    #print (u.get_dato_alfanumerico(c.regions['alliance']))
    #print (u.get_nombre_ventana(u.get_dato_alfanumerico(c.regions['title_clasificacion_poder'])))
    
    final = datetime.utcnow()
    m.logger.info (final)
    m.logger.info (f"Tiempo transcurrido: {final - comienzo}")