import utils
import cfg

def inicio():
    while not (utils.check_screen_by_icon(cfg.ICON_MAP)):
        #Puedo estar en mapa
        if (utils.check_screen_by_icon(cfg.ICON_HOME)):
            utils.click_on_location(cfg.CLICK_HOME_MAP)
        #Estoy en otra cualquier pantalla
        else:
            utils.teclado_ESC()
        utils.mover_raton_centro_pantalla()
    print ("En home")
def mapa():
    if (not utils.check_screen_by_icon(cfg.ICON_HOME)):
        inicio()
        utils.click_on_location(cfg.CLICK_HOME_MAP)
        utils.mover_raton_centro_pantalla()
    print ("Estoy en mapa")
    
def menu_gobernador ():
    while not utils.check_screeen_by_title(cfg.REGION_WINDOW_GOV_PROFILE, cfg.TITLE_WINDOW_GOV_PROFILE):
        inicio()
        utils.click_on_location(cfg.CLICK_PROFILE_MENU)
    print ("Menu gobernador")

def menu_gobernador_clasificaciones():
        while not utils.check_screeen_by_title(cfg.REGION_WINDOW_MENU_CLASIFICACIONES, cfg.TITLE_WINDOW_MENU_CLASIFICACIONES):
            menu_gobernador()
            utils.click_on_location(cfg.CLICK_PROFILE_MENU_CLASIFICACIONES)
        print ("Menu gobernador/clasificaciones")

def menu_gobernador_configuracion():
        menu_gobernador()
        utils.click_on_location(cfg.CLICK_PROFILE_MENU_CONFIGURACION)      

def menu_gobernador_clasificaciones_poder_individual():
    while not utils.check_screeen_by_title(cfg.REGION_WINDOW_POWER_STANDINGS, cfg.TITLE_WINDOW_POWER_STANDINGS):
        menu_gobernador_clasificaciones()
        utils.click_on_location(cfg.CLICK_PROFILE_MENU_CLASIFICACIONES_PODER_INDIVIDUAL)      


# import time
# time.sleep(4)
# #mapa()

# menu_gobernador_clasificaciones_poder_individual()