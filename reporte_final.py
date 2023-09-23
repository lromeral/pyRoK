import pandas as pd
import os

dir_in = "./reporte_in"
dir_out = "./reporte_out"

cont = 0
writer=  pd.ExcelWriter("reporte.xlsx")
for file in os.listdir(dir_in):
    print (file)
    file_path = os.path.join(dir_in,file)
    print (file_path)
    csvFrame = pd.read_csv(file_path)
    print ("hola")
    csvFrame.to_excel(excel_writer=writer,sheet_name=str(file),index=False)
    cont+=1
writer.close()