


import pyautogui as pa
import json


class coords:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        temp = (self.x, self.y)
        return str(temp)
     
        
 
screenSize = coords(1,1)

print (screenSize)