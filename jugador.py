from datetime import datetime
class jugador():
    def __init__(self, 
                 kd:int=0,
                 id:int=-1, 
                 pos:int=-1,
                 nombre:str='#Error#', 
                 alianza:str='#Error#', 
                 poder:int=-1, 
                 podermasalto:int=-1, 
                 kp:int=-1,
                 muertos:int=-1,
                 assist_rss:int=-1, 
                 t4kills:int=-1, 
                 t5kills:int=-1,
                 timestamp: float= datetime.timestamp(datetime.now())) -> None:
        self.__kd = kd        
        self.__id = id
        self.__pos = pos
        self.__nombre = nombre
        self.__alianza = alianza
        self.__poder = poder
        self.__podermasalto = podermasalto
        self.__kp = kp
        self.__muertos = muertos
        self.__assist_rss = assist_rss
        self.__t4kills = t4kills
        self.__t5kills = t5kills
        self.__timestamp = timestamp
    
    def __eq__(self, __value: object) -> bool:
        return self.id == object.id
    
    def __str__(self)->str:
        new_line = '\n'
        datos =(
            f'ID: {self.id} {new_line}',
            f'Position:{self.pos} {new_line}',
            f'Name: {self.nombre} {new_line}',
            f'Alliance: {self.alianza} {new_line}',
            f'Power: {self.poderactual} {new_line}',
            f'Highest Power: {self.podermasalto} {new_line}',
            f'Kill Points: {self.kp} {new_line}',
            f'Deaths: {self.muertos} {new_line}',
            f'Assist RSS: {self.assist_rss} {new_line}',
            f'T4 Kills: {self.t4kills} {new_line}',
            f'T5 Kills: {self.t5kills} {new_line}',
            f'Date: {datetime.fromtimestamp(self.__timestamp)}' 
        )
        return ''.join(datos)
            



    @property
    def id (self)->int:
        return self.__id
    @property
    def kd (self)->int:
        return self.__kd
    @property
    def pos (self)->int:
        return self.__pos
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
    def kp(self)->int:
        return self.__kp
    @property
    def muertos (self)->int:
        return self.__muertos
    @property
    def assist_rss (self)->int:
        return self.__assist_rss
    @property
    def t4kills (self)->int:
        return self.__t4kills
    @property
    def t5kills (self)->int:
        return self.__t5kills   
    @property
    def timestamp (self)->float:
        return self.__timestamp
    
    @id.setter
    def id (self, a:int)->None:
        self.__id = a
    @kd.setter
    def kd (self, a:int)->None:
        self.__kd = a
    @pos.setter
    def pos(self,a:int)->None:
        self.__pos = a
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
    @kp.setter
    def kp (self, a:int)->None:
        self.__kp=a
    @muertos.setter
    def muertos (self, a:int)->None:
        self.__muertos = a
    @assist_rss.setter
    def assist_rss(self,a:int)->None:
        self.__assist_rss = a
    @t4kills.setter
    def t4kills (self,a:int)->None:
        self.__t4kills = a
    @t5kills.setter
    def t5kills (self,a:int)->None:
        self.__t5kills = a
    @timestamp.setter
    def timestamp(self,a:float)->None:
        self.__timestamp = a

    def getJugador(self)->list:
        return [
            self.id,
            self.pos,
            self.nombre,
            self.alianza,
            self.poderactual,
            self.podermasalto,
            self.kp,
            self.muertos,
            self.assist_rss,
            self.t4kills,
            self.t5kills,
            self.timestamp
        ]
    def setInactivo(self)->None:
        self.nombre ="Inactive Player"
        self.alianza ="Inactive Player"
        self.poderactual = 0
        self.podermasalto = 0
        self.kp = 0
        self.muertos = 0
        self.assist_rss = 0
        self.t4kills = 0
        self.t5kills = 0
