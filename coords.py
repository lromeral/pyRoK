class coords:
    __cords= (0,0)
    def __init__(self, x=(0,0)) -> None:
        self.__cords = x

    def set_coords(self, x):
        self.__cords=x

    def __eq__(self, __value: object) -> bool:
        return ((self.width == __value.width) and (self.height == __value.height)) 

    def __str__(self) ->str:
        return str(self.__cords)
    
    def distanciaAB(self, x1, x2, y1, y2) -> float:
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
     
    @property
    def width (self) -> float:
        return self.__cords[0]
    @property
    def height (self) -> float:
        return self.__cords[1]
    @property
    def center (self) -> tuple:
        return self.width/2, self.height/2

