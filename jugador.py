class jugador():
    def __init__(self, id:int=0, 
                 nombre:str='ErrNombre', 
                 alianza:str='ErrAlianza', 
                 poder:int=0, 
                 podermasalto:int=0, 
                 muertos:int=0, 
                 t4kills:int=0, 
                 t5kills:int=0) -> None:        
        self.__id = id
        self.__nombre = nombre
        self.__alianza = alianza
        self.__poder = poder
        self.__podermasalto = podermasalto
        self.__muertos = muertos
        self.__t4kills = t4kills
        self.__t5kills = t5kills
    
    def __eq__(self, __value: object) -> bool:
        return self.id == object.id
    
    @property
    def id (self)->int:
        return self.__id
    @property
    def nombre (self)->str:
        return self.__nombre
    @property
    def alianza (self)->str:
        return self.__alianza
    @property
    def poderactual (self)->int:
        return self.__poder
    @property
    def podermasalto (self)->int:
        return self.__podermasalto
    @property
    def muertos (self)->int:
        return self.__muertos
    @property
    def t4kills (self)->int:
        return self.__t4kills
    @property
    def t5kills (self)->int:
        return self.__t5kills   
    
    @id.setter
    def id (self, a:int)->None:
        self.__id = a
    @nombre.setter
    def nombre (self, a:str)->None:
        self.__nombre = a.strip()
    @alianza.setter
    def alianza (self, a:str)->None:
        self.__alianza = a.strip()
    @poderactual.setter
    def poderactual (self, a:int)->None:
        self.__poder = a
    @podermasalto.setter
    def podermasalto (self, a:int)->None:
        self.__podermasalto = a
    @muertos.setter
    def muertos (self, a:int)->None:
        self.__muertos = a
    @t4kills.setter
    def t4kills (self,a:int)->None:
        self.__t4kills = a
    @t5kills.setter
    def t5kills (self,a:int)->None:
        self.__t5kills = a

    def getJugador(self)->list:
        return [
            self.id,
            self.nombre,
            self.alianza,
            self.poderactual,
            self.podermasalto,
            self.muertos,
            self.t4kills,
            self.t5kiils
        ]
    
