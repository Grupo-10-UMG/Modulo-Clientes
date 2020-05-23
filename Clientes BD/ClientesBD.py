import sqlite3
import os
import pprint
import msvcrt
#-----------------------------------------------------------------------------------------------------------
#--------------insertar registros  ---------------------
#-----------------------------------------------------------------------------------------------------------

def inserta_datos():
    miConexion=sqlite3.connect("Vehiculos")

    # para crear tabla se crea cursor
    miCursor=miConexion.cursor()

    miCursor.execute('''
        CREATE TABLE IF NOT EXISTS CLIENTES (
        ID_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE VARCHAR(50), 
        APELLIDO VARCHAR(50),
        DIRECCION VARCHAR(50),
        TELEFONO NUMBER, 
        NIT INTEGER)
    ''')

  
    #v_cod_vehiculo = int(input(f"Ingrese codigo vehiculo: "))
    c_nombre = (input(f"Ingrese nombre de cliente: "))
    c_apellido = (input(f"Ingrese apellido de cliente: "))
    c_direccion = (input(f"Ingrese direccion de cliente: "))
    c_telefono = (input(f"Ingrese telefono de cliente: "))
    c_nit = int(input(f"Ingrese NIT de cliente: "))



    #cadena =(f"""insert into INVENTARIO Values({v_cod_vehiculo},
    #'{v_marca}',
    #'{v_modelo}',
    # {v_anio},
    #'{v_descripcion}',
    # {v_cantidad},
    # {v_precio_compra}, 
    # {v_precio_venta} )""")

    #print(cadena)

    miCursor.execute(f"""INSERT INTO CLIENTES VALUES(NULL,
    '{c_nombre}',
    '{c_apellido}',
    '{c_direccion}',
    {c_telefono},
    {c_nit} )""")

    miConexion.commit()
    print("Datos guardados exitosamente! \n")
    miConexion.close()

#-----------------------------------------------------------------------------------------------------------
#-------------- Busca Registros ---------------------
#-----------------------------------------------------------------------------------------------------------
def listar():
    miConexion=sqlite3.connect("Vehiculos")
    # para crear tabla se crea cursor
    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM CLIENTES")
    
    listado_clientes=miCursor.fetchall()
    #pprint.pprint(listado_clientes)
    print( "Codigo, Nombre, Apellido, Dirección, Telefono, NIT")
    for ls_clientes in listado_clientes:
        print(ls_clientes)
    #    pprint.pprint(ls_clientes)

    
    print("Fin del listado" + '\n')

    #miConexion.close()
    
    c_cod_cliente = int(input("Ingrese el codigo del cliente que desea modificar o '0' para salir: "))
    if c_cod_cliente != 0:
        c_nombre = (input(f"Ingrese Nombre de Cliente: "))
        c_apellido = (input(f"Ingrese Apellido de Cliente: "))
        c_direccion = (input(f"Ingrese Direccion de Cliente: "))
        c_telefono = (input(f"Ingrese Telefono de Cliente: "))
        c_nit = int(input(f"Ingrese NIT de Cliente: "))
        
        miCursor.execute(f"""UPDATE CLIENTES SET
            NOMBRE = '{c_nombre}',
            APELLIDO = '{c_apellido}',
            DIRECCION = '{c_direccion}',
            TELEFONO = {c_telefono},
            NIT = {c_nit} WHERE ID_CLIENTE = {c_cod_cliente}""")

        miConexion.commit()
        print("Datos guardados exitosamente! \n")

#-----------------
#Buscar

def buscar():
    miConexion=sqlite3.connect("Vehiculos")
    # para crear tabla se crea cursor
    miCursor=miConexion.cursor()

    b_nit = int(input(f"Ingrese NIT de Cliente: "))
    
    if not b_nit:
		    print("Búsqueda inválida")
		    exit()

    sentencia = "SELECT * FROM CLIENTES WHERE NIT LIKE ?;"

    miCursor.execute(sentencia, [ "%{}%".format(b_nit) ])
    clientes=miCursor.fetchall()
    
    print(clientes)
	

    miConexion.commit()
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    miConexion.close()

#-----------------
#Eliminar

def eliminar():
    miConexion=sqlite3.connect("Vehiculos")
    # para crear tabla se crea cursor
    miCursor=miConexion.cursor()
    sentencia = "SELECT *,rowid FROM CLIENTES;"
 
    miCursor.execute(sentencia)
    
    clientes=miCursor.fetchall()
    
    print(clientes)
    
    #Pedir id del cliente a editar
    id_cliente = int(input("\nEscribe el id del cliente que quieres eliminar: "))
    if not id_cliente:
		    print("No escribiste nada")
		    exit()
 
	#Sentencia para eliminar
    sentencia = "DELETE FROM CLIENTES WHERE rowid = ?;"
 
	#Eliminar el cliente
    miCursor.execute(sentencia, [id_cliente])
    miConexion.commit()
    print("Eliminado con éxito")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    miConexion.close()
  


#-----------------------------------------------------------------------------------------------------------
#--------------Menu principal ---------------------
#-----------------------------------------------------------------------------------------------------------
c_opcion=0
while True:
	os.system("cls")

	print("Sub Menu Modulo de Clientes:" + '\n' )
	print("1. Ingreso de Nuevo Cliente" + '\n' )
	print("2. Modificacion de Registros" + '\n' )
	print("3. Busqueda por NIT" + '\n' )
	print("4. Eliminar Cliente" + '\n' )
	print("5. Salir" + '\n' )

	c_opcion = int(input("ingrese opcion: "))

	if c_opcion == 5:
		break
	#print("el valor es" + c_opcion)


	if c_opcion == 1:
		inserta_datos()
	elif c_opcion == 2:
		listar()
	elif c_opcion == 3:
            buscar()
	elif c_opcion == 4:
		eliminar()

