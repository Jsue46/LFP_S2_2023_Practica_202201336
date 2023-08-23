import os

ListaProductos = []

def Archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        return lineas



def leer_linea(linea: str):
    nombre, cantidad, *otros_datos = linea.strip().split(";")
    datos = [nombre.split()[0], nombre.split()[1], cantidad] + otros_datos
    return datos



def procesar_movimientos(nombre_archivo):
    try:
        if not nombre_archivo.endswith('.mov'):
            raise ValueError("El archivo debe tener extensión .mov")
        
        lineas = Archivo(nombre_archivo)
        
        for linea in lineas:
            dato = leer_linea(linea)
            nombre, cantidad, ubicacion = dato[1:]

            producto_encontrado = buscarV(nombre=nombre, ubicacion=ubicacion)

            if producto_encontrado:
                if dato[0] == "agregar_stock":
                    producto_encontrado["cantidad"] += int(cantidad)
                    print("\nProductos Actualizados\n")
                elif dato[0] == "vender_producto":
                    if producto_encontrado["cantidad"] >= int(cantidad):
                        producto_encontrado["cantidad"] -= int(cantidad)
                        print("\nVenta Exitosa\n")
                    else:
                        print("\nNo es posible realizar la acción. La cantidad de productos que desea vender es mayor a la existente.\n")
            else:
                print("\nEl producto no existe en ninguna bodega\n")
            
    except ValueError as ve:
        print(ve)
    except FileNotFoundError as fnfe:
        print(fnfe)



def buscarV(nombre, ubicacion):
    try:
        return next(producto for producto in ListaProductos if producto["nombre"] == nombre and producto["ubicacion"] == ubicacion)
    except StopIteration:
        return None
    


def cargar_inventario(nombre_archivo):
    try:
        if not nombre_archivo.endswith('.inv'):
            raise ValueError("ERROR: El archivo debe tener extensión .inv")
        
        lineas = Archivo(nombre_archivo)
        for linea in lineas:
            dato = leer_linea(linea)
            nombre, cantidad, precio_unitario, ubicacion = dato[1:]
            ListaProductos.append({
                "nombre": nombre,
                "cantidad": int(cantidad),
                "precio_unitario": float(precio_unitario),
                "ubicacion": ubicacion
            })

        print("\n")
        print(f"Instrucciones cargadas correctamente")
        
    except ValueError as ve:
        print(ve)
    except FileNotFoundError as fnfe:
        print(fnfe)



def crear_informe(ruta, contenido):
    try:
        if os.path.exists(os.path.dirname(ruta)):
            with open(ruta, 'w') as archivo:
                archivo.write(contenido)
            
            print("\nInforme Creado\n")
        else:
            print("Ruta inexistente")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


  
def tabla_informe() -> str:
    estructura_infome = ""

    encabezados = ["Producto", "Cantidad", "Precio Unitario", "Valor Total", "Ubicación"]
    encabezados_formatados = " | ".join(encabezados)
    separador = "-" * len(encabezados_formatados)
    
    estructura_infome += encabezados_formatados + "\n"
    estructura_infome += separador + "\n"
    
    for producto in ListaProductos:
        nombre = producto['nombre']
        cantidad = producto['cantidad']
        precio_unitario = producto['precio_unitario']
        valor_total = cantidad * precio_unitario
        ubicacion = producto['ubicacion']
        
       
        fila_formatada = "{:<8} | {:<8} | {:<15.2f} | {:<11.2f} | {:<10}".format(
            nombre, cantidad, precio_unitario, valor_total, ubicacion
        )
        
        estructura_infome += fila_formatada + '\n'
    return estructura_infome
  


while True:
  print("====================================")
  print("Lenguajes Formales y de Programación")
  print("            202201336               ")
  print("====================================")
  print("          Menú Inventario           ")
  print("1. Cargar Inventario Inicial")
  print("2. Cargar Instrucciones de Movimiento")
  print("3. Crear Informe de Inventario")
  print("4. Salir")
  opcion = input("Ingrese el número de opción:")

  if opcion == "1":
    nombre_archivo = input("Ingresa el nombre del archivo: ")
    cargar_inventario(nombre_archivo)

  elif opcion == "2":
   nombre_archivo = input("Ingresa el nombre del archivo: ")
   procesar_movimientos(nombre_archivo)

  elif opcion == "3":
   ruta = r'C:\Users\familia\OneDrive\Escritorio\Ingenieria\Lenguajes formales\LAB\Practica 1\informe_inventario.txt'
   contenido_informe = tabla_informe() 
   crear_informe(ruta, contenido_informe)

  elif opcion == "4":
   print("\n")
   print("Gracias por Visitarnos")
  
   break