import cfg as c
import utils as u
import csv

class datos_reporte:
      def __init__(self, datos:list) -> None:
            self.id = int(datos[0])
            self.name = str(datos[2])
            self.alliance = str(datos[3])
            self.position = int(datos[1])
            self.power = int(datos[4])
            self.kp = int(datos[6])
            self.deaths = int(datos[7])
            self.rss_assist = int(datos[8])
            self.t4kills = int(datos[9])
            self.t5kills = int(datos[10])
            self.timestamp = float(datos[11])

class reporte:
    def __init__(self, datos1:list, datos2:list) -> None:
        self.datos1 = datos1
        self.datos2 = datos2
    def get(self) -> list:
        pass

#csv_header 'ID', 'POSITION', 'NAME', 'ALLIANCE', 'POWER', 'HIGHEST_POWER','KP','DEATHS','RSS_ASSIST','T4_KILLS','T5_KILLS','TIMESTAMP'

'''
    ID
    NAME_+ report_ini_name
    NAME_+ report_fin_name
    
    ALLIANCE_+ report_ini_name
    ALLIANCE_+ report_fin_name
    
    POSITION_+ report_ini_name
    POSITION_+ report_fin_name
    POSITION_CHANGE

    POWER_+ report_ini_name
    POWER_+ report_fin_name
    POWER_CHANGE

    KP_+report_ini_name
    KP_+report_fin_name
    KP_CHANGE

    DEATHS_+report_ini_name
    DEATHS_+report_fin_name
    DEATHS_CHANGE

    RSS_ASSIST_+report_ini_name
    RSS_ASSIST_+report_fin_name
    RSS_ASSIST_CHANGE

    T4KILLS_+report_ini_name
    T4KILLS_+report_fin_name
    T4KILLS_CHANGE

    T5KILLS_+report_ini_name
    T5KILLS_+report_fin_name
    T5KILLS_CHANGE



'''
report_ini = c.paths['csv'] + 'reporte1.csv'
report_ini_name ="Z1"
report_fin = c.paths['csv'] + 'reporte2.csv'
report_fin_name = "Z2"
report_result = c.paths['csv'] + "report_result_" + report_ini_name + "_" + report_fin_name + ".csv" 

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
    #Agrega la fila al registro
    fr.writerow(result_row)
    #Mueve el puntero del csv al primer registro
    file2.seek(0)
    file2.readline()  

for x in no_encontrados:
     print (x.name)