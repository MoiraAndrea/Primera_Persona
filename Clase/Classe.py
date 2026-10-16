class persona:    #Molde

    def __init__(self,nombre,edad):  #constructor inicia persona creada
        self.nombre = nombre         #atributos
        self.edad = edad             #atributos
 
    def hablar  (self):                           #metodo
        print(f'{self.nombre} dice "Hola!"')
    def caminar (self):                           #metodo
        print(f'{self.nombre} esta caminando')

persona1= persona("Juan", 25)      #objeto
persona2= persona("Pepe", 12)      #objeto
persona3= persona("Moira", 23)     #objeto

persona1.hablar()
persona2.caminar()
persona3.hablar()