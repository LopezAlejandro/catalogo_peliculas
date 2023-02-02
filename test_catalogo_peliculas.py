from dominio.Pelicula import Pelicula
from servicio.Catalogo_Peliculas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print('1 - Agregar pelicula')
        print('2 - Listar peliculas')
        print('3 - Eliminar archivo de peliculas')
        print('4 - Salir')

        opcion = int(input('Ingrese su opcion (1 - 4) ---> '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el titulo de la pelicula : ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)

        elif opcion == 2:
            cp.listar_peliculas()

        elif opcion == 3:
            cp.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Salimos del programa')
