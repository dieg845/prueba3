import json

def agregar():
    Autor = [
        {
        "AutorID" : int(input("Ingresar la ID del autor : ")),
        "Nombre" : str(input("Ingresar el nombre del autor : ")),
        "Nacionalidad" : str(input("Ingresar la Nacionalidad del autor : "))
    },
    ]
    Libro = [
        {
        "LibroID" : int(input("Ingresar la ID del libro : ")),
        "Titulo" : str(input("Ingresar el nombre del libro : ")),
        "AutorID" : Autor.values[0],
        "CategoriaID" : int(input("Ingresar la ID de la categoria : ")),
        "AnoPublicacion" : int(input("Ingresar el año de publicación del libro : ")),
        "ISBN" : int(input("Ingresar la ISBN del libro : "))
    },
    ]
    Categoria = [
        {
            "CategoriaID": Libro.values[3],
            "Nombre": str(input("Ingresar la nombre de la categoria : ")),
        },
    ]
    with open("biblioteca.json","w") as biblioteca:
        json.dump(Autor,biblioteca)
        json.dump(Libro,biblioteca)
        json.dump(Categoria,biblioteca)


def editor():
    id = int(input("Busca el libro que quieres editar con su ID : "))
    with open("biblioteca.json","w") as biblioteca:
        if id in biblioteca:
            Libro = [
        {
        "LibroID" : id,
        "Titulo" : str(input("Ingresar el nombre del libro : ")),
        "AutorID" : Autor.values[0],
        "CategoriaID" : int(input("Ingresar la ID de la categoria : ")),
        "AnoPublicacion" : int(input("Ingresar el año de publicación del libro : ")),
        "ISBN" : int(input("Ingresar la ISBN del libro : "))
    },
            ]
        json.dump(Libro,biblioteca)
                       

def eliminar():
    #Esta no me salió bien porque no consigo eliminar el elemento de la lista dentro del biblioteca.json XD
    id = int(input("Busca el libro que quieres eliminar con su ID : "))
    with open("biblioteca.json","w") as biblioteca:
        if id in biblioteca:
            # json.dump(Libro.pop,biblioteca) Fue lo mejor que se me ocurrió jeje
            None

def buscar():
    #Creo que esta función también esta re mala hahaha
    id = int(input("Busca el libro que quieres buscar con su ID : "))
    with open("biblioteca.json","r") as biblioteca:
        json.load(Libro,biblioteca) 







