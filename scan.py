import jugador as j

class scan:
    def __init__(self) -> None:
        self.jugador = j()

    #Captura los datos necesarios en Mas Informacion
    def captura_info (self):
        self.logger.debug (self.captura_info.__name__)
        if (not self.u.identify_screen(c.screens['more_info'])):
            self.logger.error ("No se encuentra en la pantalla de Mas Información") 
            self.salir("No se encuentra en la pantalla de Mas Informacion")
        else:
            self.jugador.podermasalto = self.get_dato_numerico(c.regions['powerH'])
            self.jugador.muertos = self.get_dato_numerico(c.regions['deaths'])
            self.jugador.assist_rss = self.get_dato_numerico(c.regions['assist_rss'])