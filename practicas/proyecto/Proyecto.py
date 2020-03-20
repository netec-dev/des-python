#-*-coding: iso-8859-15-*-
import mysql.connector
import os

db=mysql.connector.connect(host="localhost",user="root", passwd="Welcome1", db="proyecto") 
#db=mysql.connector.connect(host="localhost",user="root", passwd="oracle_4U", db="proyecto")
#user=input("Usuario:"), passwd=input("oracle_4U"),db="proyecto")
cursor=db.cursor();
def conexion():
    cursor.execute("select version()");
    version= cursor.fetchone()
    print("la version", version);

def seleccionar():
    #tabla=input("que tabla quiere seleccionar?\n")
    stmt = "SELECT * FROM CURSO "#+tabla
    cursor.execute(stmt)
    result= cursor.fetchall()
    for row in result:
        print(row)
    x=input("pulse una tecla")
    menu()

def insertar():
    print ("insertar:\n")
    V1=input("ID:\n")
    V2=input("Nombre del curso:\n")
    V3=input("Tecnologia:\n")
    V4=input("Costo:\n")
    stmt = "insert into CURSO values('"+ V1+ "', '"+ V2+ "', '"+ V3+ "', "+ V4+ ") "
    cursor.execute(stmt)
    x=input("Insertado correctamente")
    menu()

def eliminar():
    print ("eliminar")
    V1=input("ID:\n")
    stmt = "DELETE from CURSO where ID =('"+ V1+"') "
    cursor.execute(stmt)
    x=input("Eliminado correctamente")
    menu()

def guardar():
    db.commit()
    menu()

def menu():
    os.system("cls")
    print("\n\n\t\t\t +-------------+-------------+------+-----+---------+-------+\n"
          +"\t\t\t| Field       | Type        | Null | Key | Default | Extra |\n"
          +"\t\t\t+-------------+-------------+------+-----+---------+-------+\n"
          +"\t\t\t| ID          | varchar(20) | NO   | PRI | NULL    |       |\n"
          +"\t\t\t| Nombre      | varchar(20) | YES  |     | NULL    |       |\n"
          +"\t\t\t| Tecnología  | varchar(20) | YES  |     | NULL    |       |\n"
          +"\t\t\t| Costo       | int(5)      | YES  |     | NULL    |       |\n"
          +"\t\t\t+-------------+-------------+------+-----+---------+-------+\n")

    print ("\t\t\tSeleccione la operación que desea realizar sobre la tabla CURSO")
    opcion= input ("1.-Seleccionar  \n2.-Insertar \n3.-Eliminar\n4.-Guardar\n5.-      Salir\n")
    if (opcion=="1"):
        seleccionar()
    elif (opcion=="2"):
        insertar()
    elif (opcion=="3"):
        eliminar()
    elif (opcion=="4"):
        guardar()
    else:
        print ("gracias por usar la aplicación")
        cursor.close()

conexion()
menu()
