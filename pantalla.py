from tipos import _point, _region
import cfg as c
class pantalla:
    def __init__(self, icon_loc:_point, region_titulo:_region|None , titulo:str|None, ) -> None:
        self.icon_loc =icon_loc
        self.region_titulo = region_titulo
        self.titulo = titulo

