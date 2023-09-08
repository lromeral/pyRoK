import pyautogui as pa
import cfg  
import time
import csv
import os
import pytesseract
from coords import coords
from PIL import Image, ImageGrab
from mylogger import getmylogger
    
moverA = pa.moveTo
obtener_posicion = pa.position
pauto=pa


class utilesRoK:

    
    logger = getmylogger(__name__)

    def __init__(self) -> None:
        self.moverA = pa.moveTo
        self.pytesseract = pytesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        
    def capturar_region(self,region)->Image:
        self.logger.debug (self.capturar_region.__name__)
        captura = ImageGrab.grab(bbox=region)
        return captura
    
    def screenshot (self,strPath:str)->Image:
        self.logger.debug (self.capturar_region.__name__)
        self.logger.info ("Capturando pantana en " + strPath)
        return pa.screenshot(strPath,region=cfg.regions['screenshots'])

    def click (self)->None:
        self.logger.debug (self.click.__name__)
        time.sleep(0.1)
        pa.click()
        time.sleep(0.1)

    def crearCarpeta(self,path:str):
        self.logger.debug (self.crearCarpeta.__name__)
        self.logger.info  ("Creando carpeta en: " + path)
        try:
            os.mkdir(path)
        except:
            self.logger.critical ("No se pudo crear el directorio " +  path)
            exit(-1)

    def identify_screen(self,img:Image)->bool:
        self.logger.debug (self.identify_screen.__name__)
        time.sleep(0.5)
        self.logger.info ("Identificando pantalla: " + str(img))
        intentos=0
        max_intentos = 10
        while (pa.locateOnScreen(img,confidence=cfg.scan['confidence']) == None and intentos <= max_intentos):
            self.logger.warning ("Warn: Imagen no encontrada. Reintentando #" + str(intentos))
            intentos +=1
            time.sleep(1)

        if (intentos >= max_intentos):
            self.logger.critical ("Imagen no encontrada.")
            return False
        else:
            self.logger.info ("Imagen encontrada")
            return True
        
    def procesar_pantalla(self,img:Image, hacer_click:bool=True)->coords:
        self.logger.debug (self.procesar_pantalla.__name__)
        if (not self.identify_screen(img)):
            self.logger.critical ("Finalizando")
            exit(-1)
        else:
            zero = pa.locateOnScreen(img,confidence=cfg.scan['confidence'])
            self.logger.info ("Moviendo a imagen encontrada...")
            pa.moveTo(zero.left + zero.width/2, zero.top + zero.height/2,duration=3)
            if hacer_click:self.click()
            return coords((zero.left,zero.top))
    
    def write_to_csv(self,data:list, fichero, header:list):
        self.logger.debug (self.write_to_csv.__name__)
        if (not os.path.exists(fichero)):
            self.logger.info ("Creando fichero csv")
            file = open (file = fichero ,mode='w', newline='', encoding="utf-8")
            wr = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
            wr.writerow(header)
            wr.writerow(data)
        else:
            file = open (file = fichero ,mode='a', newline='', encoding="utf-8")
            self.logger.info ("Guardando datos en fichero csv")
            wr = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
            wr.writerow(data)