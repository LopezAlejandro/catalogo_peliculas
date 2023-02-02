import os


class CatalogoPeliculas:
    ruta_archivo = '/home/ale/Cursos/Python/Archivos/catalogo_peliculas/peliculas.txt'

    @classmethod
    def agregar_peliculas(cls, pelicula):
        with open(cls.ruta_archivo, 'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r') as archivo:
            print('Catalogo de Peliculas'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo {cls.ruta_archivo} borrado')
