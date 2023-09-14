import csv
from datos_reporte import datos_reporte
from datetime import datetime

def human_format(num):
    num = float('{:.5g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


origen_name = '3043_20230911_144420_data.csv'
destino_name = '3043_20230911_144420_data_simple.csv'

origen = open (file = origen_name,mode='r', newline='', encoding="utf-8")
datos_origen = csv.reader(origen)


fresult = open(file=destino_name, mode='w', newline='',encoding="utf-8")
fr=csv.writer(fresult)

#Header
fr.writerow(datos_origen.__next__())

for row in datos_origen:
    data = datos_reporte(row)
    new_row = [
        data.id,
        data.position,
        data.name,
        data.alliance,
        human_format(data.power),
        human_format(data.powerH),
        human_format(data.kp),
        human_format(data.deaths),
        human_format(data.rss_assist),
        human_format(data.t4kills),
        human_format(data.t5kills),
        datetime.utcfromtimestamp(data.timestamp)
    ]
    fr.writerow(new_row)