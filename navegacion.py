import utils
import cfg
import time

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


def ir_inicio():
    while not (is_inicio() or is_mapa()):
        utils.teclado_ESC()
    if (is_mapa()):
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



# time.sleep(4)
# ir_perfil_gobernador_clasificaciones_poder_individual()