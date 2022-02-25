#los booleando bool son objetos de tipo verdadero falso
verdadero=True
falso=False

#resumen de operadores
#  and   - solo si ambos son True
#  or    - solo si alguno o ambos son True
#  ^     -  xor   - solo si solamente uno es True
#  not   - convierte False en True y visceversa

print("\n PRUEBA AND  ------------------")
print(True   and  True)
print(False  and  False)
print(True   and  False)

print("\n PRUEBA OR --------------------")
print(True   or  True)
print(False  or  False)
print(False  or  True)

print("\n PRUEBA XOR -------------------")
print(True   ^   True )
print(False  ^   False)
print(True   ^   False)

print("\n PRUEBA NOT -------------------")
print(not(True))
print(not(False))

# Se pueden utilizar los operadores and y or 
# con varios argumentos

print("=======================================")

print("\n varios argumentos \n")
print( True and True and True and True and False)
print( False or False or False or False or True)

print("=======================================")

# se pueden utilizar operadores de comparacion
#
#    Operadores Logicos
#   ====================
#
#    >   mayor que             <  menor que
#    >=  mayor igual que       <= menor igual que
#    ==  igual que             != diferente que
#
#   Nota == y != se pueden usar no solo para valores numericos
# 

print("\ncomparando valores\n")

print(333 > 0) # es verdad 333 es mayor que 0
print(999 < 0) # es falso 999 no es mayor que 0
print("texto" == "texto") # es verdadero son strings iguales









