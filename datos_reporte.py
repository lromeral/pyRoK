class datos_reporte:
    def __init__(self, datos:list) -> None:
            self.__id = int(datos[0])
            self.__name = str(datos[2])
            self.__alliance = str(datos[3])
            self.__position = int(datos[1])
            self.__power = int(datos[4])
            self.__powerH = int(datos[5])
            self.__kp = int(datos[6])
            self.__deaths = int(datos[7])
            self.__rss_assist = int(datos[8])
            self.__t4kills = int(datos[9])
            self.__t5kills = int(datos[10])
            self.__timestamp = float(datos[11])
    @property
    def id (self)->int:
        return self.__id
    @id.setter   
    def id (self,a:int)->None:
        self.__id = a    

    @property
    def name (self)->str:
        return self.__name
    @name.setter   
    def name (self,a:str)->None:
        self.__name = a    

    @property
    def timestamp (self)->float:
        return self.__timestamp 
    @timestamp.setter   
    def timestamp (self,a:float)->None:
        self.__timestamp = a

    @property
    def alliance (self)->str:
        return self.__alliance
    @alliance.setter   
    def alliance (self,a:str)->None:
        self.__alliance = a    
    
    @property
    def position (self)->int:
        return self.__position
    @position.setter   
    def position (self,a:int)->None:
        self.__position = a

    @property
    def power (self)->int:
        return self.__power
    @power.setter   
    def power (self,a:int)->None:
        self.__power = a

    @property
    def powerH (self)->int:
        return self.__powerH
    @powerH.setter   
    def powerH (self,a:int)->None:
        self.__powerH = a

    @property
    def kp (self)->int:
        return self.__kp
    @kp.setter   
    def kp (self,a:int)->None:
        self.__kp = a

    @property
    def deaths (self)->int:
        return self.__deaths
    @deaths.setter   
    def deaths (self,a:int)->None:
        self.__deaths = a
    
    @property
    def rss_assist (self)->int:
        return self.__rss_assist
    @rss_assist.setter   
    def rss_assist (self,a:int)->None:
        self.__rss_assist = a

    @property
    def t4kills (self)->int:
        return self.__t4kills    
    @t4kills.setter   
    def t4kills (self,a:int)->None:
        self.__t4kills = a
    
    @property
    def t5kills (self)->int:
        return self.__t5kills 
    @t5kills.setter   
    def t5kills (self,a:int)->None:
        self.__t5kills = a
    def to_list(self)->list:
        return [self.__id,
            self.__name,
            self.__alliance,
            self.__position,
            self.__power,
            self.__powerH,
            self.__kp,
            self.__deaths,
            self.__rss_assist,
            self.__t4kills,
            self.__t5kills,
            self.__timestamp]