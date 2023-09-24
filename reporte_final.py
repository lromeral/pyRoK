import pandas as pd
import os
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

def get_reino_from_filename(filename:str)->str:
    result = filename[:filename.find("_")]
    return result

def get_kd_stats(filepath:str)->dict:
    origen = open (file = filepath,mode='r', newline='', encoding="utf-8")
    datos_origen = csv.reader(origen)

    #Header
    datos_origen.__next__()
    kd_stats = {
        "power": 0,
        "kp": 0,
        "deaths":0,
        "t4kills":0,
        "t5kills":0,
    }        
    for row in datos_origen:
        kd_stats['power'] += int(row[4]) 
        kd_stats['kp']+= int(row[6])
        kd_stats['deaths']+=int(row[7])
        kd_stats['t4kills']+=int(row[9])
        kd_stats['t5kills']+=int(row[10])

    return kd_stats

def append_kd_stats_xls(archivo:str,stats:dict):
    fresult = open(file=archivo, mode='a', newline='',encoding="utf-8")
    fr=csv.writer(fresult)
    header = list(stats.keys())
    data = list(stats.values())
    fr.writerow(header)
    fr.writerow(data)


def generate_xls(archivo:str, directorio_in):
    writer=  pd.ExcelWriter(archivo)
    for file in os.listdir(directorio_in):
        print (file)
        file_path = os.path.join(dir_in,file)
        #RawData
        sheet_name = get_reino_from_filename(file)
        append_sheet(writer,sheet_name,file_path)
        #Human Readable Data
        sheet_simple = sheet_name + "_Simple"
        workbook = writer.book
        workbook.create_sheet(sheet_simple)
        worksheet_simple = workbook.get_sheet_by_name(sheet_simple)
        df = pd.read_excel(workbook,sheet_name,header=1)
        for row in df:
            print(row)
        append_sheet(writer,get_reino_from_filename(sheet_simple),file_path)
    writer.close()

def append_sheet(excel_writer, sheet_name:str, archivo_csv):
        csvFrame = pd.read_csv(archivo_csv)
        csvFrame.to_excel(excel_writer=excel_writer,sheet_name=sheet_name,index=False)

def append_sheet_simple (excel_writer, sheet_name:str, archivo_csv):
        csvFrame = pd.read_csv(archivo_csv)
        print (csvFrame)
        #csvFrame.to_excel(excel_writer=excel_writer,sheet_name=sheet_name,index=False)

def generate_sheet_hr(arhivo:str):
    pass

def filter_power_kp_relation (file_in,relation:float, below=True):
     
    origen = open (file = file_in,mode='r', newline='', encoding="utf-8")
    datos_origen = csv.reader(origen)

    filename = os.path.splitext(file_in)[0]

    file_out =  filename
    file_out +=  "_below_" if below else "_above_"
    file_out += str(relation) + ".csv"

    fresult = open(file=file_out, mode='w', newline='',encoding="utf-8")
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
            datetime.utcfromtimestamp(data.timestamp),
            data.kp/data.power if data.power > 0 else 0
        ]
        if (below):
            if (new_row[12] <=relation): fr.writerow(new_row)
        else:
            if (new_row[12] >=relation): fr.writerow(new_row)



filter_power_kp_relation("3131_20230922_222803_data.csv",2.0)

# dir_in = "./csv/test"
# dir_out = "./reporte_out"
# archivo_out = "prueba.xlsx"

# #generate_xls(archivo_out,dir_in)

# csvf = pd.read_csv("./csv/test/3135_20230923_123625_data.csv")

# for i in csvf.index:
#     row = [(csvf['ID'][i], 
#                csvf['POSITION'][i],
#                csvf['NAME'][i],
#                csvf['ALLIANCE'][i],
#                human_format(int(csvf['POWER'][i])),
#                human_format(int(csvf['HIGHEST_POWER'][i])),
#                human_format(int(csvf['KP'][i])),
#                human_format(int(csvf['DEATHS'][i])),
#                human_format(int(csvf['RSS_ASSIST'][i])),
#                human_format(int(csvf['T4_KILLS'][i])),
#                human_format(int(csvf['T5_KILLS'][i])))]
#     print (row)


