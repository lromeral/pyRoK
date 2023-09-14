##REGIONES DE ESCANEO DE DATOS en formato tupla bbox
##(left_x, top_y, right_x, bottom_y)
#REGIONES DE BUSQUEDA 
regions = dict(
    #id =(1070,270,1220,310),
    id =(1050,270,1220,320),
    name=(925,310,1200,345),
    alliance=(905,410,1145,445),
    power = (1160,415,1400,460),
    #power=(1130,225,1260,250),
    powerH=(1400,345,1621,375),
    kp_more_info=(1600,220,1730,250),
    kp_profile = (1410,415,1665,450),
    deaths=(1400,530,1680,555),
    assist_rss =(1400,760,1680,790),
    #t4kills=(1135,480,1300,515),
    t4kills=(1127,480,1400,520),
    #t5kills=(1135,530,1300,555),
    t5kills=(1127,520,1400,560),
    screenshots=(320,1600,80,900),
    title_gobernador = (860,165,1380,235),
    title_clasificacion_poder = (740,125,1480,165),
    title_mas_informacion = (740,125,1480,165)
)

titulos = dict(
    perfil_gob ="pereiil del gorernador",
    mas_info = "MAS INFORMACION",
    classificacion = "CLASIFICACION DE PODER INDIVIDUAL"
)

csv_header = [
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

pos_clasificacion = list([
    (0,0),
    (610,370),
    (610,470),
    (610,570),
    (610,670),
    (610,770),
])


posiciones = dict(
    info_kp = (1440,393),
    mas_info = (670,813),
    cerrar_mas_info = (1715, 135),
    cerrar_perfil =(1685,185),
    kills = (1400, 236),
    copy_name_mas_info =(710,235),
    copy_name_profile = (1060,330)
)
base_path='./'

#PATHS
paths=dict(
    images= base_path +  'images/',
    patterns= base_path + 'patterns/',
    screenshots=base_path + 'screenshots/',
    csv=base_path + 'csv/'
)
#GAME CONF
game = dict(
  width= 1600,
  height= 900
)

#SCAN OPTIONS
scan = dict(
    first_pos= (610,370),
    start=1,
    end = 10,
    #Espacio entre las columnas de la clasificacion general para el desplazamiento de los 4 primeros
    standings_space = 100,
    #Para pa.locateimage
    confidence = 0.95
)

#PATTERNS TO IDENTIFY SCREENS
patterns = dict(
  profile_pic= 'icon_profile_pic.png',
  classifications= 'icon_clasificaciones.png',
  classifications_power= 'icon_clasificaciones_poder_2.png',
  more_info= 'icon_masinformacion.png',
  info_kp= 'icon_infokp.png',
  close= 'icon_cerrar_perfil.png',
  copy_name= 'icon_copy_name.png'
)

#SCREENS
screens = dict(
  profile= paths['images'] + 'pantalla_perfil_gobernador_2.png',
  more_info= paths['images'] + 'pantalla_mas_informacion.png',
  kd_standings_power =paths['images'] + 'pantalla_clasificacion_poder.png'
)

#ICONS
icons = dict(
    profile =  paths['images'] +  'icon_profile_pic.png', 
    standings = paths['images'] +  'icon_clasificaciones.png',
    power = paths['images'] +  'icon_clasificaciones_poder.png',
    close =  paths['images'] +  'icon_cerrar_perfil.png'
)


tesseract = dict(
    path = "C:\Program Files\Tesseract-OCR",
    #cfg_only_numbers = '--psm 7 --oem 1 -c tessedit_char_whitelist=0123456789',
    cfg_only_numbers = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789 lang="spa"',
    cfg_alphanumeric = '--psm 7 --oem 3'
)