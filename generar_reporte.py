import cfg as c
import utils as u
import csv
from datetime import datetime

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


    
class datos_info:
    def __init__(self, report_name:str, report_date: float=0) -> None:
        self.num_jugadores = 0
        self.report_name = report_name
        self.report_date = datetime.fromtimestamp(report_date)
        self.total_power =0
        self.average_power = 0
        self.total_kp = 0
        self.average_kp=0 
        self.total_t4kills = 0
        self.average_t4kills = 0
        self.total_t5kills = 0
        self.average_t5kills = 0


    def add_data(self, raw_data:datos_reporte)->None:
        self.num_jugadores +=1
        self.total_power += raw_data.power
        self.total_kp += raw_data.kp
        self.total_t4kills += raw_data.t4kills
        self.total_t5kills += raw_data.t5kills

        if (self.num_jugadores ==1): self.report_date = datetime.fromtimestamp(raw_data.timestamp)

    def get_data(self)->list:
        
        self.average_kp = round (self.total_kp / self.num_jugadores,2)
        self.average_power = round (self.total_power / self.num_jugadores,2)
        self.average_t4kills = round (self.total_t4kills / self.num_jugadores,2)
        self.average_t5kills = round (self.total_t5kills / self.num_jugadores,2)
        
        datos = list ([
            self.report_name,
            self.report_date,
            self.num_jugadores,
            self.total_power,
            self.average_power,
            self.total_kp,
            self.average_kp,
            self.total_t4kills,
            self.average_t4kills,
            self.total_t5kills,
            self.average_t5kills
        ])
        return datos

    def get_header(self) ->list:
        info_header = list([
            'REPORT NAME',
            'REPORT DATE',
            'PLAYERS',
            'TOP300 TOTAL POWER',
            'TOP300 AVERAGE POWER',
            'TOP300 TOTAL KP',
            'TOP300 AVERAGE KP',
            'TOP300 TOTAL T4KILLS',
            'TOP300 AVERAGE T4KILLS',
            'TOP300 TOTAL T5KILLS',
            'TOP300 AVERAGE T5KILLS'
        ])

        return info_header


class reporte:
    def __init__(self, datos1:list, datos2:list) -> None:
        self.datos1 = datos1
        self.datos2 = datos2
    def get(self) -> list:
        pass


report_ini = c.paths['csv'] + 'reporte1.csv'
report_ini_name ="Z1"
report_fin = c.paths['csv'] + 'reporte2.csv'
report_fin_name = "Z2"
report_result = c.paths['csv'] + "report_result_" + report_ini_name + "_" + report_fin_name + ".csv" 

#csv_header 'ID', 'POSITION', 'NAME', 'ALLIANCE', 'POWER', 'HIGHEST_POWER','KP','DEATHS','RSS_ASSIST','T4_KILLS','T5_KILLS','TIMESTAMP'
csv_header = list ([
    'ID',
    f'NAME_{report_ini_name}',
    f'NAME_{report_fin_name}',
    f'ALLIANCE_{report_ini_name}',
    f'ALLIANCE_{report_fin_name}',
    f'POSITION_{report_ini_name}',
    f'POSITION_{report_fin_name}',
    f'POSITION_CHANGE',
    f'POWER_{report_ini_name}',
    f'POWER_{report_fin_name}',
    f'POWER_CHANGE',
    f'KP_{report_ini_name}',
    f'KP_{report_fin_name}',
    f'KP_CHANGE',
    f'DEATHS_{report_ini_name}',
    f'DEATHS_{report_fin_name}',
    f'DEATHS_CHANGE',
    f'RSS_ASSIST_{report_ini_name}',
    f'RSS_ASSIST_{report_fin_name}',
    f'RSS_ASSIST_CHANGE',
    f'T4KILLS_{report_ini_name}',
    f'T4KILLS_{report_fin_name}',
    f'T4KILLS_CHANGE',
    f'T5KILLS_{report_ini_name}',
    f'T5KILLS_{report_fin_name}',
    f'T5KILLS_CHANGE'
])



f1_total_power = 0
f1_top300_total_kp = 0
f1_top300_total_t4kills = 0
f1_top300_total_t5kills = 0

f2_total_power = 0
f2_top300_total_kp = 0
f2_top300_total_t4kills = 0
f2_top300_total_t5kills = 0


file1 = open (file = report_ini ,mode='r', newline='', encoding="utf-8")
file1.readline()
f1 = csv.reader(file1)

file2 = open (file = report_fin ,mode='r', newline='', encoding="utf-8")
file2.readline()
f2 = csv.reader(file2)

fresult = open(file=report_result, mode='w', newline='',encoding="utf-8")
fr=csv.writer(fresult)
fr.writerow(csv_header)


no_encontrados = list()
encontrado = False

info1 = datos_info(report_name=report_ini_name, report_date=0)
info2 = datos_info(report_name=report_fin_name, report_date=0)


for x in f1:
    print (x)
    encontrado = False
    #Dato a buscar
    global d1
    d1 = datos_reporte(x)
    print ("procesando id: " + str(d1.id))
    for y in f2:
        global d2
        d2=datos_reporte(y)
        if (d1.id==d2.id and d2.id != -1):
            #print (f"Encontrado: {d1.id} con nombre: {d1.name}")
            encontrado = True
            #agrega la linea a csv de resultado
            break
    if not encontrado: 
         no_encontrados.append(d1)
    result_row = list ([
                 d1.id,
                 d1.name,
                 d2.name,
                 d1.alliance,
                 d2.alliance,
                 d1.position,
                 d2.position,
                 d2.position - d1.position,
                 d1.power,
                 d2.power,
                 d2.power - d1.power,
                 d1.kp,
                 d2.kp,
                 d2.kp - d1.kp,
                 d1.deaths,
                 d2.deaths,
                 d2.deaths - d1.deaths,
                 d1.rss_assist,
                 d2.rss_assist,
                 d2.rss_assist -d1.rss_assist,
                 d1.t4kills,
                 d2.t4kills,
                 d2.t4kills - d1.t4kills,
                 d1.t4kills,
                 d2.t5kills,
                 d2.t5kills - d1.t5kills
            ])
    #Prepara datos para estadisticas
    info1.add_data(d1)
    info2.add_data(d2)
    #Agrega la fila al registro
    fr.writerow(result_row)
    #Mueve el puntero del csv al primer registro
    file2.seek(0)
    file2.readline()  

#Graba el header
fr.writerow(list())
fr.writerow (info1.get_header())
fr.writerow(info1.get_data())
fr.writerow(info2.get_data())


for x in no_encontrados:
     print (x.name)