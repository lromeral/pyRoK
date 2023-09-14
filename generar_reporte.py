import cfg as c
import utils as u
import csv

from datetime import datetime
from datos_reporte import datos_reporte
from datos_info import datos_info
    
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