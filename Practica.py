#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno.  Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
   
    def __init__(self, nombre, nota):
       
        self.nombre = nombre
        self.nota = nota

  
  #Metodos

    def imprimir (self, nombre):
        print(f"Nombre del alumno: {self.nombre}")
    
    def resultado (self, nota):
        print(f"Nota del alumno: {self.nota}")
        if nota >= 5:
            print (f"Aprobado")
        else:
            print (f"Suspenso")



alumno1 = Alumno("Raquel",9)
alumno2 = Alumno ("Juan",10)
alumno3 = Alumno ("Carla",7)

   
    alumno1.imprimir()
    alumno1.resultado()
    alumno2.imprimir()
    alumno2.resultado()
    alumno3.imprimir()
    alumno3.resultado()