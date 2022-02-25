# una forma de ordenar los elementos es usando objetos tipo LIST
# son elementos entre corchetes rectangulares [] y con elementos entre comas
# una lista es un grupo ordenado de elementos que contienen todo tipo de objetos
# numeros, booleandos, otras listas, etc etc etc
listaEnBlanco=[]
listaConUnElemento=[1]
listaConVariosElementos=[1,2,3,4.44444,1+2j,"texto",["OTRA",1,"LISTA"]]
#---------------------------------------------------
#analizando como se trabaja con valores de una lista
print("\n Declarando y operando con listas")

print("--------------------------------------------\n")
lista=[11,22,33,44,55,66,77,88,99,["x","y","z"]]
print(" lista   : "+str(      lista       )+"\n")

#analizando su dimension con len -> retorna int

print(" dimension len(lista) : "+str(     len(lista)   )+"\n")

#para acceder al primer elemento usar 0
# OJO. empieza desde 0 no desde 1

print(" elem 0  : "+str(      lista[0]    ))
print(" elem 1  : "+str(      lista[1]    ))
print(" elem 2  : "+str(      lista[2]    ))
print(" elem 3  : "+str(      lista[3]    ))
print(" elem 4  : "+str(      lista[4]    ))
print(" elem 5  : "+str(      lista[5]    ))
print(" elem 6  : "+str(      lista[6]    ))
print(" elem 7  : "+str(      lista[7]    ))
print(" elem 8  : "+str(      lista[8]    ))
print(" elem 9  : "+str(      lista[9]    ))
print("\n  si hay sublistas se puede acceder directamente\n")
print(" elem 9.0 : "+str(   lista[9][0]   ))
print(" elem 9.1 : "+str(   lista[9][1]   ))
print(" elem 9.2 : "+str(   lista[9][2]   ))

#analizando los 
print("\nPara recorrer el ciclo al reves usar simbolos negativos desde -1 \n")

print(" elem -1  : "+str(      lista[-1]    ))
print(" elem -2  : "+str(      lista[-2]    ))
print(" elem -3  : "+str(      lista[-3]    ))
print(" elem -10  : "+str(     lista[-10]   ))

