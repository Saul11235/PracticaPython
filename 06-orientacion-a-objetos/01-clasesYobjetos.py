#La POO es un apradigma de programacion
#Clase : abstraccion de un tipo de objeto
#Objeto: conjunto de datos y funcionalidades relacionados a una entidad 
#En python las clases tambien son objetos

#Vamos a crear una clase
class rectangulo:
    "Vamos a definir una clase de objeto tipo rectangulo"

    def __init__(self,ancho,alto):
        #Esta es la funcion self.init(ancho,alto) es la primera en ejecutarse cuando
        #se crea un nuevo objeto
        self.X=ancho
        self.Y=alto
        print("Tenemos un rectangulo de "+str(self.X)+" x "+str(self.Y))

#-------------------------------------------------------------
#Vamos a crear dos objetos de la clase rectangulo

Figura1=rectangulo(11,22)
Figura2=rectangulo(100,500)


