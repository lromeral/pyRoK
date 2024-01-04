import utils
import cfg
import time
import cv2
import numpy as np

def identificar_pantalla():
    for posicion in cfg.TITULOS_LOCALIZACION:
        d = utils.datos_alfanumericos (utils.capture_region(posicion.value))
        if cfg.TitulosPantallas.has_value(d):
            return cfg.TitulosPantallas(d).name
    return cfg.TitulosPantallas.TITLE_WINDOW_DESCONOCIDO.name

def is_inicio()->bool:
     return utils.check_screen_by_icon(cfg.ICON_MAP)
def is_mapa()->bool:
    return utils.check_screen_by_icon(cfg.ICON_HOME)
def is_menu_gobernador()->bool:
    return utils.check_screeen_by_title(cfg.REGION_WINDOW_GOV_PROFILE, cfg.TitulosPantallas.GOV_PROFILE.value, retries=1)
def is_menu_gobernador_clasificaciones()->bool:
     return utils.check_screeen_by_title(cfg.REGION_WINDOW_MENU_CLASIFICACIONES, cfg.TitulosPantallas.CLASIFICACIONES.value, retries=1)
def is_menu_gobernador_clasificaciones_poder_individual()->bool:
     return utils.check_screeen_by_title(cfg.REGION_WINDOW_POWER_STANDINGS, cfg.TitulosPantallas.POWER_STANDINGS.value, retries=1)
def is_perfil_gobernador_configuracion()->bool:
     return utils.check_screeen_by_title(cfg.REGION_WINDOW_POWER_STANDINGS, cfg.TitulosPantallas.CONFIGURACION.value, retries=1)
def is_perfil_gobernador_configuracion_personajes()->bool:
     return utils.check_screeen_by_title(cfg.TITULOS_LOCALIZACION.MEDIO.value, cfg.TitulosPantallas.PERSONAJES.value, retries=1)
def is_perfil_gobernador_configuracion_personajes_inicio()->bool:
     return utils.check_screeen_by_title(cfg.TITULOS_LOCALIZACION.INICIO_PERSONAJES.value, cfg.TitulosPantallas.INICIO_SESION_PERSONAJE.value, retries=1)

def ir_inicio():
    while not (is_inicio() or is_mapa()):       
        print ("ni inicio ni mapa") 
        utils.teclado_ESC()
        #utils.click()
    if (is_mapa()):
        print ("ir_inicio->es_mapa")
        utils.click_on_location(cfg.CLICK_HOME_MAP) 


def ir_perfil_gobernador():
    if not is_menu_gobernador():
        ir_inicio()
        utils.click_on_location(cfg.CLICK_PROFILE_MENU)

def ir_perfil_gobernador_clasificaciones():
    if is_menu_gobernador_clasificaciones():
        return
    else:
        ir_perfil_gobernador()
    time.sleep(0.5)
    utils.click_on_location(cfg.CLICK_PROFILE_MENU_CLASIFICACIONES)

def ir_perfil_gobernador_clasificaciones_poder_individual():
    if is_menu_gobernador_clasificaciones_poder_individual():
        return
    else:
        ir_perfil_gobernador_clasificaciones()
    time.sleep(0.5)
    utils.click_on_location(cfg.CLICK_PROFILE_MENU_CLASIFICACIONES_PODER_INDIVIDUAL)

def ir_perfil_gobernador_configuracion():
    if is_perfil_gobernador_configuracion():
        return
    else:
        ir_perfil_gobernador()
    time.sleep(0.5)
    utils.click_on_location(cfg.CLICK_PROFILE_MENU_CONFIGURACION)

def ir_perfil_gobernador_configuracion_personajes():
    if is_perfil_gobernador_configuracion_personajes():
        return
    else:
        ir_perfil_gobernador_configuracion()
    time.sleep(0.5)
    utils.click_on_location(cfg.CLICK_PROFILE_MENU_CONFIGURACION_PERSONAJES)

def ir_perfil_gobernador_configuracion_personajes_inicio():
    if is_perfil_gobernador_configuracion_personajes():
        return
    else:
        ir_perfil_gobernador_configuracion()
    time.sleep(0.5)
    utils.click_on_location(cfg.CLICK_PROFILE_MENU_CONFIGURACION_PERSONAJES)

def buscar_reino(numero_reino:int)->bool:
    intentos = 0
    while True:
        if is_perfil_gobernador_configuracion_personajes():
            break
        else:
            time.sleep(5)
            intentos +=1
            if intentos > 5:
                ir_perfil_gobernador_configuracion_personajes()
                break

    utils.mover_raton_centro_pantalla()
    cadena_busqueda = numero_reino
    #Captura la pantalla de clasificaciones:
    img_pil = utils.capture_region(cfg.REGION_CROP_REINOS,False)
    img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    #cv2.imshow("image", img)
    #cv2.waitKey(0)    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert = 255 - gray

    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(invert, -1, sharpen_kernel)
    #thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    imagen_analizada = invert
    # cv2.imshow("result",result)
    # cv2.imshow("gray",gray)
    # cv2.imshow("sharpen",sharpen)
    # cv2.imshow("invert",invert)
    # cv2.imshow("imagen analizada",imagen_analizada)
    # cv2.waitKey(0)

    d = utils.pytesseract.image_to_data(imagen_analizada, output_type=utils.pytesseract.Output.DICT,config=" --psm 6 -c tessedit_char_whitelist=0123456789")
    
    print (d)

    texts = d['text']
    lefts = d['left']
    tops = d ['top'] 

    texts2 = list([])
    tops2 = list([])
    lefts2 = list([])

    #Crea listas solo con numeros validos
    for i in range(0,len(texts)):
        print (f"i:{i}")
        if (texts[i].isdigit() and len(texts[i])==4):
            texts2.append(int(texts[i]))
            tops2.append(tops[i])
            lefts2.append(lefts[i])

    for i in range(0,len(texts2)):
        print (f"i:{i}")
        print(f"Buscando: {cadena_busqueda} contra {texts2[i]}")
        if (texts2[i]==cadena_busqueda):
            print (lefts2[i])
            print (tops2[i])
            left_screenshot =  cfg.REGION_CROP_REINOS[0] + lefts2[i]
            top_screenshot= cfg.REGION_CROP_REINOS[1] + tops2[i]
            return (left_screenshot, top_screenshot)

    direccion = True #Siempre hacia abajo

    DESPLAZAMIENTO_SCROLL = 10
    utils.scroll(DESPLAZAMIENTO_SCROLL,direccion)
    print ("despues del scroll")
    #Vuelta a buscar
    return buscar_reino(cadena_busqueda)


def abrir_reino (reino:int):
    ir_perfil_gobernador_configuracion_personajes()
    time.sleep(1)
    posicion = buscar_reino(reino)
    utils.click_on_location(posicion)
    if is_perfil_gobernador_configuracion_personajes_inicio():
        utils.click_on_location(cfg.CLICK_PROFILE_MENU_CONFIGURACION_PERSONAJES_INICIO)
        time.sleep(5)
    while True:
        print ("esperando")
        #Puede ser el inicio o que este ya en el reino que se necesita
        if (is_inicio() or is_mapa()):
            print ("Inicio o Mapa")
            break
        elif (is_perfil_gobernador_configuracion_personajes()):
            print ("Ya esta en el")
            ir_inicio()
            break
        else:
            print ("timer")
            time.sleep(30)
            ir_inicio()
            #utils.click()