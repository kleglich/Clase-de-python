
def agregar_usuario(usuarios):
    nombre = input("Ingrese el nombre del usuario a agregar: ")
    usuarios.append(nombre)
    print(f"Usuario '{nombre}' agregado")
    
def extender_usuario(usuarios):
    invitado = input("Ingrese el nombre del usuarioinvitado ").split()
    usuarios.extend(invitado)   
    print(f"Usuarios {invitado} agregados")
    
def incertar_usuario(usuarios):
    nombre = input("Ingrese el nombre del usuario a insertar: ")
    posicion = int(input("Ingrese la posición donde insertar: "))
    usuarios.insert(posicion, nombre)
    print(f"Usuario '{nombre}' insertado en la posición {posicion}")
    
def eliminar_usuario(usuarios):
    nombre = input("Ingrese el nombre del usuario a eliminar: ")
    if nombre in usuarios:
        usuarios.remove(nombre)
        print(f"Usuario '{nombre}' eliminado")
    else:
        print("Usuario no encontrado")

def pop_usuario(usuarios):
    if usuarios:
        posicion = int(input("Ingrese la posición a eliminar de la lista de usuarios: "))
        if posicion == -1:
            eliminado = usuarios.pop()
        else:
            eliminado = usuarios.pop(posicion)
        print(f"Usuario '{eliminado}' eliminado")
    else:
        print("La lista está vacia")

    
def index_usuario(usuarios):
    nombre = input("Ingrese el nombre del usuario para buscar su índice: ")
    if nombre in usuarios:
        print(f"El índice de '{nombre}' es {usuarios.index(nombre)}")
    else:
        print("Usuario no encontrado")
    
def count_usuario(usuarios):
    nombre = input("Ingrese el nombre del usuario para contar: ")
    cantidad = usuarios.count(nombre)
    print(f"El usuario '{nombre}' aparece {cantidad} veces")
    
def ordenar_usuario(usuarios):
    usuarios.sort()
    print("Usuarios ordenados alfabéticamente")

def reverse_usuario(usuarios):
    usuarios.reverse()
    print("Lista de usuarios invertida")

def mostrar_usuarios(usuarios):
    print("Usuarios actuales:", usuarios)


def menu():
    usuarios = []
    while True:
        print("*** Menu de Usuarios ***")
        print("1. Agregar usuario (append)")
        print("2. Extender usuarios (extend)")
        print("3. Insertar usuario (insert)")
        print("4. Eliminar usuario (remove)")
        print("5. Eliminar usuario por posición (pop)")
        print("6. Buscar índice de usuario (index)")
        print("7. Contar usuario (count)")
        print("8. Ordenar usuarios (sort)")
        print("9. Invertir lista de usuarios (reverse)")
        print("10. Mostrar usuarios")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                agregar_usuario(usuarios)
            case "2":
                extender_usuario(usuarios)
            case "3":
                incertar_usuario(usuarios)
            case "4":
                eliminar_usuario(usuarios)
            case "5":
                pop_usuario(usuarios)
            case "6":
                index_usuario(usuarios)
            case "7":
                count_usuario(usuarios)
            case "8":
                ordenar_usuario(usuarios)
            case "9":
                reverse_usuario(usuarios)
            case "10":
                mostrar_usuarios(usuarios)
            case "0":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida, intente de nuevo.")

#**********************************************************************#

menu()