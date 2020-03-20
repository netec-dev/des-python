# [P112]
# -*- coding: utf-8 -*-
import mysql.connector
import os
# pip install mysql-connector-python
#db = mysql.connector.connect(user='root', password='woola', host='127.0.0.1', port='3307')
db=mysql.connector.connect(host="localhost",user="root", passwd="Welcome1", db="proyecto") 
cursor = db.cursor()
cursor.execute("SELECT version()")
version = cursor.fetchone()
print("La versión de la base de datos es %s" %version)
db.close()

# [P116]
##-*-coding: iso-8859-15-*-
#import mysql.connector
#db=mysql.connector.connect(user='root', password='woola', host='127.0.0.1', port='3307',database='pruebaspython')
db=mysql.connector.connect(host="localhost",user="root", passwd="Welcome1", db="proyecto") 
cursor=db.cursor()
cursor.execute("SELECT nombre FROM alumno WHERE rfc='RFC002'")
datos=cursor.fetchone()
print("El dato encontrado es: %s" %datos)
db.close()
# [P117]
#-*-coding: iso-8859-15-*-
#import mysql.connector
#db=mysql.connector.connect(user='root', password='woola', host='127.0.0.1', port='3307',database='pruebaspython')
db=mysql.connector.connect(host="localhost",user="root", passwd="Welcome1", db="proyecto") 
cursor=db.cursor()
cursor.execute("INSERT INTO alumno VALUES('RFC007','James',100)")
print("Elemento insertado correctamente")
db.commit()
db.close()

# [P118]
#-*-coding: iso-8859-15-*-
#import mysql.connector
#db=mysql.connector.connect(user='root', password='woola', host='127.0.0.1', port='3307',database='pruebaspython')
db=mysql.connector.connect(host="localhost",user="root", passwd="Welcome1", db="proyecto") 
cursor=db.cursor()
cursor.execute("DELETE FROM alumno WHERE rfc='RFC007'")
print("Elemento eliminado correctamente")
db.commit()
db.close()
# [P119]
#-*-coding: iso-8859-15-*-
#import mysql.connector
#db=mysql.connector.connect(user='root', password='woola', host='127.0.0.1', port='3307',database='pruebaspython')
db=mysql.connector.connect(host="localhost",user="root", passwd="Welcome1", db="proyecto") 
cursor=db.cursor()
cursor.execute("UPDATE alumno SET nombre='Nombre MODIFICADO' WHERE rfc='RFC001'")
print("Elemento actualizado correctamente")
db.commit()
db.close()

