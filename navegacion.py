from pantalla import pantalla
import utils as u
def acceder_pantalla(p:pantalla)->bool:
    #Ir al punto
    u.moverA(p.icon_loc)
    #Hacer click
    u.click()
    #Chequear si estoy en pantalla
    return u.check_screeen(p.region_titulo,p.titulo)
