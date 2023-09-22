
import cv2
import numpy as np
import time
from PIL import Image, ImageEnhance, ImageGrab
from typing_extensions import TypeAlias
import utils as u
import cfg as c

#left_x, top_y, right_x, bottom_y
_region: TypeAlias = tuple[int, int, int, int]
_point: TypeAlias = tuple[int,int]


#WINDOWS
REGION_WINDOW_GOV_PROFILE = _region((860,165,1380,235))
REGION_WINDOW_MORE_INFO = _region((740,125,1480,165))
REGION_WINDOW_POWER_STANDINGS = _region ((740,125,1480,165))

time.sleep(5)

captura_original = ImageGrab.grab(bbox=REGION_WINDOW_GOV_PROFILE)
captura_primer_paso = cv2.cvtColor(np.array(captura_original), cv2.COLOR_BGR2GRAY)
thresh_img = cv2.threshold(captura_primer_paso, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]



print (u.datos_alfanumericos(thresh_img))



cv2.imshow("hola",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()