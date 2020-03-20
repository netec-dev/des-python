# PRÁCTICA 8
# El ejercicio consiste en crear una clase llamada persona, que va a tener como atributos "nombre" y "edad", con dos métodos, uno para obtener el nombre (que lo imprima por pantalla) y otro para obtener la edad
# Después crear una clase llamada alumno que herede de Persona, aparte de tener la edad y el nombre , agregar el atributo "calificación" con un método para consultar la nota
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def getNombre(self):
        print("nombre: " + self.nombre)
        return self.nombre
    def getEdad(self):
        print("edad: " + self.edad)
        return self.edad
#
objPersona = Persona("Juan", "López")
objPersona.getNombre()
objPersona.getEdad()

class Alumno(Persona):
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def getCalificacion(self):
        print("calificacion: " + str(self.calificacion))
        return self.calificacion

objAlumno = Alumno("Nombre", "Apellido", 10)
objAlumno.getNombre()
objAlumno.getEdad()
objAlumno.getCalificacion()