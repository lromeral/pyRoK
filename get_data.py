import cv2
import numpy as np
import pytesseract
import cfg
import jugador
import datetime
import mylogger
import utils

class get_data:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    
    def __init__(self) -> None:
        self.logger = mylogger.getmylogger(__name__)

    def alliance (self,img)->str:
        y=cfg.REGION_DATA_PROFILE_ALLIANCE[1]
        x=cfg.REGION_DATA_PROFILE_ALLIANCE[0]
        h=cfg.REGION_DATA_PROFILE_ALLIANCE[3] - cfg.REGION_DATA_PROFILE_ALLIANCE[1]
        w=cfg.REGION_DATA_PROFILE_ALLIANCE[2] - cfg.REGION_DATA_PROFILE_ALLIANCE[0]

        image = cv2.imread(img)
        crop = image[y:y+h, x:x+w]

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        invert = 255 - gray
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        #cv2.imshow('gray', gray)
        #cv2.imshow('invert', invert)
        #cv2.imshow('sharpen', sharpen)
        #cv2.imshow('thresh', thresh)
        #cv2.waitKey()
        # Perform text extraction
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 --oem 3').strip()
        return data

    def power (self,img)->int:
        y=cfg.REGION_DATA_PROFILE_POWER[1]
        x=cfg.REGION_DATA_PROFILE_POWER[0]
        h=cfg.REGION_DATA_PROFILE_POWER[3] - cfg.REGION_DATA_PROFILE_POWER[1]
        w=cfg.REGION_DATA_PROFILE_POWER[2] - cfg.REGION_DATA_PROFILE_POWER[0]

        image = cv2.imread(img)
        crop = image[y:y+h, x:x+w]

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        invert = 255 - gray
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        #cv2.imshow('gray', gray)
        #cv2.imshow('invert', invert)
        #cv2.imshow('sharpen', sharpen)
        #cv2.imshow('thresh', thresh)
        #cv2.waitKey()
        # Perform text extraction
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
        return int(data)
    
    def powerh (self,img)->int:
        y=cfg.REGION_DATA_MORE_INFO_POWERH[1]
        x=cfg.REGION_DATA_MORE_INFO_POWERH[0]
        h=cfg.REGION_DATA_MORE_INFO_POWERH[3] - cfg.REGION_DATA_MORE_INFO_POWERH[1]
        w=cfg.REGION_DATA_MORE_INFO_POWERH[2] - cfg.REGION_DATA_MORE_INFO_POWERH[0]

        image = cv2.imread(img)
        crop = image[y:y+h, x:x+w]

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        invert = 255 - gray
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        #cv2.imshow('gray', gray)
        #cv2.imshow('invert', invert)
        #cv2.imshow('sharpen', sharpen)
        #cv2.imshow('thresh', thresh)
        #cv2.waitKey()
        # Perform text extraction
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
        return int(data)
    def id (self,img)->int:
        y=cfg.REGION_DATA_PROFILE_GOV_ID[1]
        x=cfg.REGION_DATA_PROFILE_GOV_ID[0]
        h=cfg.REGION_DATA_PROFILE_GOV_ID[3] - cfg.REGION_DATA_PROFILE_GOV_ID[1]
        w=cfg.REGION_DATA_PROFILE_GOV_ID[2] - cfg.REGION_DATA_PROFILE_GOV_ID[0]

        image = cv2.imread(img)
        crop = image[y:y+h, x:x+w]

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        invert = 255 - gray
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        #cv2.imshow('gray', gray)
        #cv2.imshow('invert', invert)
        #cv2.imshow('sharpen', sharpen)
        #cv2.imshow('thresh', thresh)
        #cv2.waitKey()

        # Perform text extraction
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
        return int(data)

    def deads (self,img)->int:
    
        y=cfg.REGION_DATA_MORE_INFO_DEATHS[1]
        x=cfg.REGION_DATA_MORE_INFO_DEATHS[0]
        h=cfg.REGION_DATA_MORE_INFO_DEATHS[3] - cfg.REGION_DATA_MORE_INFO_DEATHS[1]
        w=cfg.REGION_DATA_MORE_INFO_DEATHS[2] - cfg.REGION_DATA_MORE_INFO_DEATHS[0]

        image = cv2.imread(img)
        crop = image[y:y+h, x:x+w]

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        invert = 255 - gray
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # cv2.imshow('gray', gray)
        # cv2.imshow('invert', invert)
        # cv2.imshow('sharpen', sharpen)
        # cv2.imshow('thresh', thresh)
        # cv2.waitKey()

        # Perform text extraction
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
        return int(data)
    
    def rss_assist (self,img)->int:
    
        y=cfg.REGION_DATA_MORE_INFO_RSS_ASSIST[1]
        x=cfg.REGION_DATA_MORE_INFO_RSS_ASSIST[0]
        h=cfg.REGION_DATA_MORE_INFO_RSS_ASSIST[3] - cfg.REGION_DATA_MORE_INFO_RSS_ASSIST[1]
        w=cfg.REGION_DATA_MORE_INFO_RSS_ASSIST[2] - cfg.REGION_DATA_MORE_INFO_RSS_ASSIST[0]

        image = cv2.imread(img)
        crop = image[y:y+h, x:x+w]

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


        #invert = 255 - sharpen
        #cv2.imshow('gray', gray)
        #cv2.imshow('invert', invert)
        #cv2.imshow('sharpen', sharpen)
        #cv2.imshow('thresh', thresh)
        #cv2.waitKey()

        # Perform text extraction
        data = pytesseract.image_to_string(thresh, config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789').strip()
        print (data)
        return int(data)



    def kp (self,img)->int:
    
        y=cfg.REGION_DATA_PROFILE_KP[1]
        x=cfg.REGION_DATA_PROFILE_KP[0]
        h=cfg.REGION_DATA_PROFILE_KP[3] - cfg.REGION_DATA_PROFILE_KP[1]
        w=cfg.REGION_DATA_PROFILE_KP[2] - cfg.REGION_DATA_PROFILE_KP[0]

        image = cv2.imread(img)
        crop = image[y:y+h, x:x+w]

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        invert = 255 - gray
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # cv2.imshow('gray', gray)
        # cv2.imshow('invert', invert)
        # cv2.imshow('sharpen', sharpen)
        # cv2.imshow('thresh', thresh)
        # cv2.waitKey()

        # Perform text extraction
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
        return int(data)


    def t4k (self,img)->int:

        y=cfg.REGION_DATA_KP_T4[1]
        x=cfg.REGION_DATA_KP_T4[0]
        h=cfg.REGION_DATA_KP_T4[3] - cfg.REGION_DATA_KP_T4[1]
        w=cfg.REGION_DATA_KP_T4[2] - cfg.REGION_DATA_KP_T4[0]

        image = cv2.imread(img)
        crop = image[y:y+h, x:x+w]

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        invert = 255 - gray
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # cv2.imshow('gray', gray)
        # cv2.imshow('invert', invert)
        # cv2.imshow('sharpen', sharpen)
        # cv2.imshow('thresh', thresh)
        # cv2.waitKey()

        # Perform text extraction
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
        return int(data)

    def t5k (self,img)->int:
    
        y=cfg.REGION_DATA_KP_T5[1]
        x=cfg.REGION_DATA_KP_T5[0]
        h=cfg.REGION_DATA_KP_T5[3] - cfg.REGION_DATA_KP_T5[1]
        w=cfg.REGION_DATA_KP_T5[2] - cfg.REGION_DATA_KP_T5[0]

        image = cv2.imread(img)
        crop = image[y:y+h, x:x+w]

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        invert = 255 - gray
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # cv2.imshow('gray', gray)
        # cv2.imshow('invert', invert)
        # cv2.imshow('sharpen', sharpen)
        # cv2.imshow('thresh', thresh)
        # cv2.waitKey()

        # Perform text extraction
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
        return int(data)

    def get_nombre_from_file (self,txt_file_path:str)->str:
        try:
            with open(txt_file_path,mode='r',encoding="utf-8") as f:
                name = f.read()
                return name
        except FileNotFoundError:
            return "InactivePlayer"

    def get_timestamp_from_file (self,txt_file_path:str)->float:
        try:
            with open(txt_file_path,mode='r',encoding="utf-8") as f:
                data = f.read()
                return float(data)
        except FileNotFoundError:
            return datetime.timestamp(datetime.utcnow())
    
    def get_csv_path(self)->str:
        return self.filename_csv
      
    def start (self, dir_in:str, dir_out:str='', inicio:int=1, final:int=300)->bool:
            try:
                kdname = dir_in[16:20]
                self.filename_csv = f"{cfg.SCANS_PATH}/{dir_in}/{dir_in}.csv"
                screeshots_location = f"{cfg.SCANS_PATH}/{dir_in}/{cfg.SCREENSHOTS_PATH}"

                #print (screeshots_location)

                for posicion in range(inicio,final+1):
                    j = jugador.jugador()

                    img_profile_path = f"{screeshots_location}/{kdname}_{posicion}{cfg.PROFILE_FILE_SUFIX}" 
                    img_more_info_path = f"{screeshots_location}/{kdname}_{posicion}{cfg.MORE_INFO_FILE_SUFIX}" 
                    img_kp_path = f"{screeshots_location}/{kdname}_{posicion}{cfg.KP_FILE_SUFIX}" 
                    txt_file_path = f"{screeshots_location}/{kdname}_{posicion}{cfg.NAME_FILE_SUFIX}" 
                    txt_timestamp_path =f"{screeshots_location}/{kdname}_{posicion}{cfg.TIMESTAMP_FILE_SUFIX}" 


                    #print (img_profile_path)

                    if (utils.checkPath(img_profile_path) and utils.checkPath(img_more_info_path)):
                        j.kd = kdname
                        j.pos = posicion
                        j.id = self.id(img_profile_path)
                        j.nombre= self.get_nombre_from_file(txt_file_path)
                        j.alianza = self.alliance(img_profile_path)
                        j.poderactual = self.power(img_profile_path)
                        j.podermasalto = self.powerh(img_more_info_path)
                        j.kp = self.kp(img_profile_path)
                        j.muertos=self.deads(img_more_info_path)
                        j.rss_assist = self.rss_assist(img_more_info_path)

                        j.t4kills = self.t4k(img_kp_path)
                        j.t5kills = self.t5k(img_kp_path)

                        j.timestamp = self.get_timestamp_from_file(txt_timestamp_path)

                        self.logger.debug(j)    
                    
                        utils.write_to_csv(data=j.getJugador(), fichero= self.filename_csv, header=cfg.CSV_HEADER)
                return True
            except Exception as e:
                print ("Exception")
                print (e)
                return False

#g = get_data()
#dir = '20231012_202222_3131_test'
# img_profile = './scans/20231008_214958_3131/screenshots/3131_200_profile.png'
# img_kp = './scans/20231008_214958_3131/screenshots/3131_200_kp.png'
# img_moreinfo = './scans/20231008_214958_3131/screenshots/3131_200_more_info.png'
# txt_name = './scans/20231008_214958_3131/screenshots/3131_200_name.txt'


# print (f"ID: {g.id(img_profile)}")
# print (f"Alianza: {g.alliance(img_profile)}")
# print (f"POWER: {g.power(img_profile)}")
# print (f"POWER H: {g.powerh(img_moreinfo)}")
# print (f"DEADS: {g.deads(img_moreinfo)}")
# print (f"RSS: {g.rss_assist(img_moreinfo)}")
# print (f"T4: {g.t4k(img_kp)}")
# print (f"T5: {g.t5k(img_kp)}")
#g.start (dir_in=dir, dir_out=None,inicio=30,final=301)