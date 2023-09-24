import pandas as pd
import os

dir_in = "./reporte_in"
dir_out = "./reporte_out"


def get_reino_from_filename(filename:str)->str:
    result = filename[:filename.find("_")]
    return result

def generate_report():
    writer=  pd.ExcelWriter("reporte.xlsx")
    for file in os.listdir(dir_in):
        print (file)
        file_path = os.path.join(dir_in,file)
        print (file_path)
        csvFrame = pd.read_csv(file_path)
        csvFrame.to_excel(excel_writer=writer,sheet_name=get_reino_from_filename(file),index=False)
    writer.close()


generate_report()