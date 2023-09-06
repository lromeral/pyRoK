##REGIONES DE ESCANEO DE DATOS en formato tupla bbox
##(left_x, top_y, right_x, bottom_y)
#REGIONES DE BUSQUEDA 
regions = dict(
    id ='(1079,281,1200,310)',
    name='(925,310,1200,345)',
    alliance=(920,400,1200,450),
    #poderactual = (1190,415,1400,440),
    power='(1130,225,1260,250)',
    powerH='(1400,345,1621,375)',
    deaths='(1400,530,1621,555)',
    t4kills='(1143,485,1300,510)',
    t5kills='(1143,530,1300,555)',
    screenshots='(320,1600,80,900)'
)

posiciones = dict(
    info_kp = (1440,393),
    mas_info = (670,813),
    cerrar_mas_info = (1715, 135),
    cerrar_perfil =(1685,185),
    kills = (1400, 236),
    copy_name =(700,235),
    copy_name2 = (1060,330)
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
    confidence = 0.9
)

#PATTERNS TO IDENTIFY SCREENS
patterns = dict(
  profile_pic= 'icon_profile_pic.png',
  classifications= 'icon_clasificaciones.png',
  classifications_power= 'icon_clasificaciones_poder.png',
  more_info= 'icon_masinformacion.png',
  info_kp= 'icon_infokp.png',
  close= 'icon_cerrar_perfil.png',
  copy_name= 'icon_copy_name.png'
)

#SCREENS
screens = dict(
  profile= paths['images'] + 'pantalla_perfil_gobernador.png',
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
    cfg_only_numbers = '--psm 7 --oem 1 -c tessedit_char_whitelist=0123456789',
    cfg_alphanumeric = '--psm 10 --oem 3'
)