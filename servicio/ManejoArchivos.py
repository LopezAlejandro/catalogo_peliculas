class ManejoArchivos:
    def __init__(self,nombre):
        self.nombre = nombre

    def __enter__(self):
        self.nombre = open(self.nombre,'a')
        return self.nombre

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.nombre:
            self.nombre.close()