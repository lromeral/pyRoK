import time
from datetime import datetime
from scan import scan
import utils as u
import cfg as c

if __name__=='__main__':
    kd = input("Nombre del Reino: ")
    i = int (input("Inicio: "))
    f = int(input('Final: ')) +1
    time.sleep(5)
    m = scan(kdname=kd, inicio=i ,final=f)
    comienzo = datetime.utcnow()
    m.logger.info (comienzo)
    
    m.start()

    #print (u.get_dato_numerico(c.regions['t4kills']))
    #print (u.get_dato_alfanumerico(c.regions['alliance']))
    #print (u.get_nombre_ventana(u.get_dato_alfanumerico(c.regions['title_clasificacion_poder'])))
    
    final = datetime.utcnow()
    m.logger.info (final)
    m.logger.info (f"Tiempo transcurrido: {final - comienzo}")


#time.sleep(3)
#u.capture_region (c.REGION_WINDOW_GOV_PROFILE).show()

#u.capture_cv(c.REGION_WINDOW_GOV_PROFILE)
#print (u.datos_numericos(u.capture_region (c.DATA_ID, True)))
#u.capture_region(c.DATA_ID).show()


#print (u.is_ventana(c.REGION_WINDOW_GOV_PROFILE,c.TITLE_WINDOW_POWER_STANDINGS))

'''
from PIL import Image, ImageEnhance
time.sleep(3)
captura_in = ImageEnhance.Contrast(u.capture_region(c.DATA_ID).convert('L'))
captura_out = captura_in.enhance(3)
captura_out.show()
input()
print (u.datos_numericos(captura_out))
'''




#if (not u.check_screeen(c.REGION_WINDOW_GOV_PROFILE, c.TITLE_WINDOW_GOV_PROFILE)): print ("Entra")






