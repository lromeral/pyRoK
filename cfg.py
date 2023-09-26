from tipos import _region, _point
from pantalla import pantalla
class location():
    def __init__(self, region:_region, title:str|None=None) -> None:
        self.region = region
        self.title = title
    def __str__(self) -> str:
        return "Region:" + str(self.region) + " title:" + str(self.title)


BASE_PATH='./'
SCANS_PATH = BASE_PATH + 'scans/'
SCREENSHOTS_PATH='screenshots/'

#PATHS
PATHS=dict(
    IMAGES= BASE_PATH +  'images/',
    CSV=BASE_PATH + 'csv/'
)

TESSERACT = dict(
    PATH = "C:\Program Files\Tesseract-OCR",
    ONLY_NUMBERS = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789',
    ALPHANUMERIC = '--psm 7 --oem 3'
)
#WINDOWS
TITLE_WINDOW_GOV_PROFILE = "PERFIL DEL GOBERNADOR"
TITLE_WINDOW_MORE_INFO = "MAS INFORMACION"
TITLE_WINDOW_POWER_STANDINGS = "CLASIFICACION DE PODER INDIVIDUAL"
TITLE_WINDOW_CONFIGURACION ="CONFIGURACION"
TITLE_WINDOW_PERSONAJES = "PERSONAJES"

#WINDOWS
REGION_WINDOW_GOV_PROFILE = _region((860,165,1380,235))
REGION_WINDOW_MORE_INFO = _region((740,125,1480,165))
REGION_WINDOW_POWER_STANDINGS = _region ((740,125,1480,165))
REGION_WINDOW_CONFIGURACION =_region((0,0,0,0))
REGION_WINDOW_PERSONAJES = _region((0,0,0,0))


#WHERE IS THE DATA TO COLLECT
DATA_ID = _region((1040,270,1220,318))
DATA_NAME = _region((925,310,1200,345))
DATA_ALLIANCE = _region((910,410,1165,445))
DATA_POWER = _region((1160,415,1400,460))
DATA_POWERH = _region((1400,345,1630,380))
DATA_KP = _region ((1410,415,1665,450))
DATA_DEATHS = _region ((1400,530,1630,560))
DATA_RSS_ASSIST = _region((1400,760,1630,790))
DATA_T4KILLS = _region((1127,480,1400,520))
DATA_T5KILLS = _region ((1127,520,1400,560))

#WHERE HAVE TO CLICK
CLICK_INFO_KP = _point((1440,393))
CLICK_MORE_INFO = _point((670,813))
CLICK_CLOSE_MORE_INFO = _point((1715, 135))
CLICK_CLOSE_GOV_PROFILE = _point((1685,185))
CLICK_KILLS_STATS = _point((1400, 236))
CLICK_COPY_NAME = _point((710,235))

#PUNTOS PANTALLAS PANTALLAS
POINT_PANTALLA_INICIO =_point((0,0))
POINT_PANTALLA_MAS_INFO =_point((0,0))
POINT_PANTALLA_PERFIL_GOBERNADOR = _point((0,0))
POINT_PANTALLA_CONFIGURACION = _point((0,0))
POINT_PANTALLA_PERSONAJES = _point((0,0))

#SCREENSHOTS
SCREENSHOT_DATA = _region((320,90,1890,970))
SCREENSHOT_STANDINGS = _region((475,110,1730,950))
SCREENSHOT_GOV_PROFILE = _region((510,160,1700,900))
SCREENSHOT_MORE_INFO = _region((475,110,1730,950))

#
pantalla_inicio = pantalla(POINT_PANTALLA_INICIO,None,None)
pantalla_perfil_gobernador = pantalla(POINT_PANTALLA_PERFIL_GOBERNADOR,REGION_WINDOW_GOV_PROFILE,TITLE_WINDOW_GOV_PROFILE)
pantalla_mas_info = pantalla(POINT_PANTALLA_MAS_INFO,REGION_WINDOW_MORE_INFO,TITLE_WINDOW_MORE_INFO)
pantalla_configuracion = pantalla(POINT_PANTALLA_CONFIGURACION,REGION_WINDOW_CONFIGURACION,TITLE_WINDOW_CONFIGURACION)
pantalla_personajes = pantalla(POINT_PANTALLA_PERSONAJES,REGION_WINDOW_PERSONAJES,TITLE_WINDOW_PERSONAJES)


#(0,+100)
STANDING_POS = list([
    (0,0),
    (610,370),#Primera
    (610,470),#Segunda
    (610,570),#Tercera
    (610,670),#a partir de la cuarta
    (610,770),#Quinta
    (610,870)#Sexta y ultima
])

CSV_HEADER = [
    'ID',
    'POSITION',
    'NAME',
    'ALLIANCE',
    'POWER',
    'HIGHEST_POWER',
    'KP',
    'DEATHS',
    'RSS_ASSIST',
    'T4_KILLS',
    'T5_KILLS',
    'TIMESTAMP'
]
