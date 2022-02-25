#Analizando strings o cadenas de texto
#
# se puede usar comillas simples '' o comillas dobles ""
# dentro de una cadena "\n" cuenta como salto de pagina
# poner una r o u antes para hacer cadena raw o unicode
#
cadena    ="hola soy una cadenaNormal\nsalto"
cadenaRaw =r"hola soy una cadenaRaw\nsalto"
cadenaUni =u"Holä soy una cadena unicode"
#
#Nota.- salto de pagina "\n" tabulador "\t"
#  
print("\n\tProbando Strings\n")
print("------------------------------------")

print(cadena)
print("")
print(cadenaRaw)
print("")
print(cadenaUni)
#
#Nota.- tambien se puede guardar strings en varias lineas
#       usando triple """ o triple '''
#
print("------------------------------------")

stringVariasL="""hola soy un archivo
de varias lineas
sigo """

print(stringVariasL)
print("------------------------------------")
#
# Nota.- tambien se pueden operar con * y + con strings
#
print("Ejemplo suma")
print("HOLA "+" ESTOY "+" SUMANDO "+" CADENAS ")
print()  
print("Ejemplo multiplicacion")
print(30*"HOLA ")
#
# Nota.- si es necesario convertir otro valor a string
#        utilizar la funcion str
#
print("-----------------------------------")
# si ejecutaramos print("texto"+numero)
# dara error recuerda que python es fuertemente tipado
print("una centena es: "+str(100))

