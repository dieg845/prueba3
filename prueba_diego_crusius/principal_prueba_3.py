import mantenedor_prueba_3 
import reportes_prueba_3

def mantenedor():
    print("*******************************\n")
    print("*      MANTENEDOR LIBRO       *\n")
    print("*******************************\n\n\n")
    print("| 1 | Agregar libro")
    print("| 2 | Editor libro")
    print("| 3 | Eliminar libro")
    print("| 4 | Buscar libro")
    print("| 5 | Volver")
    opcionm = int(input("Seleccionar una opción : "))

    if opcionm == 1:
        mantenedor_prueba_3.agregar()
    
    if opcionm == 2:
        mantenedor_prueba_3.editor()
    
    if opcionm == 3:
        mantenedor_prueba_3.eliminar()
    
    if opcionm == 4:
        return mantenedor_prueba_3.buscar()
            
    if opcionm == 5:
        return principal()
    
    else:
        print("Por favor seleccionar una opción válida")
        return mantenedor()

def reportes():
    return reportes_prueba_3.reportes()

def principal():
    print("*******************************\n")
    print("*       MUNDO LIBRO            *\n")
    print("*******************************\n\n\n")
    print("| 1 | Mantenedor de libros")
    print("| 2 | Reportes")
    print("| 3 | Salir")
    opcion = int(input("Seleccionar una opción : "))

    if opcion == 1 :
        return mantenedor()
    
    if opcion == 2 :
        return reportes()
    
    if opcion == 3 :
        return "Muchas gracias por su visita a Mundo Libro"
    
    else:
        print("Por favor seleccionar una opción válida")
        return principal()
    
    
print(principal())



