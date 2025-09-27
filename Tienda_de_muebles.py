
def agregar_cliente(clientes):
    codigo = input("Código del cliente: ")
    nombre = input("Nombre del cliente: ")
    email = input("Email del cliente: ")
    clientes.append((codigo, nombre, email, [])) 
    print("Cliente agregado")

def ver_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados")
    else:
        for cliente in clientes:
            print(f"Código: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}, Facturas registradas: {len(cliente[3])}")

def eliminar_cliente(clientes):
    codigo = input("Código del cliente a eliminar: ")
    for i, cliente in enumerate(clientes):
        if cliente[0] == codigo:
            clientes.pop(i)
            print("Cliente eliminado.")
            return
    print("Cliente no encontrado.")

def agregar_factura(clientes, codigo_cliente):
    for cliente in clientes:
        if cliente[0] == codigo_cliente:
            codigo = input("Código de la factura: ")
            fecha = input("Fecha: ")
            monto = float(input("Monto total: "))
            items = int(input("Cantidad de ítems: "))
            cliente[3].append((codigo, fecha, monto, items))
            print("Factura agregada")
            return
    print("Cliente no encontrado")

def ver_facturas(clientes, codigo_cliente):
    for cliente in clientes:
        if cliente[0] == codigo_cliente:
            if not cliente[3]:
                print("No hay facturas registradas para este cliente")
            else:
                print(f"Facturas de {cliente[1]} (Código: {cliente[0]})")
                for factura in cliente[3]:
                    print(f"Código: {factura[0]}, Fecha: {factura[1]}, Monto: {factura[2]}, Ítems: {factura[3]}")
            return
    print("Cliente no encontrado")

def menu_facturas(clientes, codigo_cliente):
    while True:
        print("\n****MENÚ FACTURAS****")
        print("1. Agregar Factura")
        print("2. Ver Facturas")
        print("3. Volver al Menú Principal")
        opcion = input("Elige una opción: ")
        print("\n")
        
        match opcion:
            case "1":
                agregar_factura(clientes, codigo_cliente)
            case "2":
                ver_facturas(clientes, codigo_cliente)
            case "3":
                break
            case _:
                print("Opción inválida, elija una que este en el menu")


def menu_principal():
    clientes = []  

    while True:
        print("\n****MENÚ PRINCIPAL****")
        print("1. Agregar Cliente")
        print("2. Ver Clientes")
        print("3. Eliminar Cliente")
        print("4. Gestionar Facturas")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        print("\n")

        match opcion:
            case "1":
                agregar_cliente(clientes)
            case "2":
                ver_clientes(clientes)
            case "3":
                eliminar_cliente(clientes)
            case "4":
                codigo = input("Código del cliente: ")
                menu_facturas(clientes, codigo)
            case "5":
                print("El programa cerro")
                break
            case _:
                print("Opción inválida, elija una que este en el menu")

#################################################################
menu_principal()


