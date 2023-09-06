import utils as u
import jugador as j
import cfg as c
import time
import datetime

class main():
    def __init__(self) -> None:
        #Jugador que será analizado


        self.main()

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
            #Salir
            pass

    #Captura los datos del Perfil del Gobernador
    def captura_profile (self):
        if (not u.identify_screen(c.screens['profile'])): 
            self.salir("No se encuentra la pantalla de perfil del gobernador")
        else:
            #Captura de datos en PERFIL
            ####Alianza
            u.capturar_region(c.regions['alliance'])

            #Salir
            pass
    #Cierra la pantalla de Perfil del Gobernador
    def cerrar_perfil(self):
        if u.identify_screen(c.screens['profile']):
            u.moverA(c.posiciones['cerrar_perfil'],duration=0.5)
            u.click()
        else:
            self.salir("No se encuentra la pantalla de perfil del gobernador")

    #Cierra la pantalla de Mas Información
    def cerrar_mas_info(self):
        if u.identify_screen(c.screens['more_info']):
            u.moverA(c.posiciones['cerrar_mas_info'],duration=0.5)
            u.click()
        else:
            self.salir("No se encuentra la pantalla Mas Informacion")

    def copiar_nombre_more_info(self):
        if u.identify_screen(c.screens['more_info']):
            u.moverA(c.posiciones['copy_name'],duration=0.3)
            u.click()
        else:
            self.salir("No se encuentra la pantalla Mas Informacion")

    def copiar_nombre_profile(self):
        if u.identify_screen(c.screens['profile']):
            u.moverA(c.posiciones['copy_name2'],duration=0.3)
            u.click()
        else:
            self.salir("No se encuentra la pantalla Mas Informacion")


    #Procesa el jugador en cuestion
    def procesa_jugador(self,num, posicion)->None:
        global jugador
        jugador = j.jugador()
        if (u.identify_screen(c.screens['kd_standings_power'])):
            print ("Procesando Perfil #" + str(num+1))
            # Mueve el raton a las coordenadas del primer jugador
            u.moverA(posicion, duration=0.5)
            u.click()
        else:
            self.salir("No se encuentra en la pantalla de clasificaciones poder individual")
        #Captura datos del perfil
        self.captura_profile()
        #Copia el nombre
        self.copiar_nombre_profile()
        ##Dentro del perfil accede a Mas informacion
        self.accede_mas_info()
        ##Captura datos de Mas Informacion
        self.captura_info()
        ## Detalle kills
        self.accede_estadisticas_asesinato()
        ###Vuelve al perfil del jugador
        self.cerrar_mas_info()
        ##Mas info kp
        self.cerrar_perfil()

    #Aborta el programa con mensaje en consola
    def salir (self, mensaje:str):
        print (mensaje)
        exit(-1)
    
    #Programa principal
    def main(self)->bool:
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
        for x in range(0,30):
            print ("Procesando jugadores")
            if (x<=3): posicion = c.scan['first_pos'][0],c.scan['first_pos'][1] + x * c.scan['standings_space']
            self.procesa_jugador(x, posicion)
        return True

if __name__=='__main__':
    time.sleep(5)
    comienzo = datetime.datetime.now()
    print (comienzo)
    main()
    final =datetime.datetime.now()
    print (final)
    print (f"Tiempo transcurrido: {final - comienzo}")