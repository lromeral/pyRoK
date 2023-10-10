class WindowNotFound(Exception):
    def __init__(self, *args: object, capture:bool=False, filepath:str) -> None:
        super().__init__(*args)
        if capture: pass
