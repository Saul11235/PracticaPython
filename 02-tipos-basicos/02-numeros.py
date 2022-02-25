#datos basicos - numeroso
#creando nuevos datos enteros

#La capacidad depende de si un numero es de 32 o 64 bits
#    32 bits rango:   -2^31 hasta 2^31
#    64 bits rango:   -2^63 hasta 2^63
# para casos generales es raro pasar estos limites

print("\nnumero entero")
entero=111
print(entero)
print(type(entero))

# Nota.-
# para casos donde era necesario guardar valores mas grandes
# en python 2 existia el tipo long poniendo una L al final
# long ya no es soportado en python3 por ser poco eficiente 
# existian tambien otros numeros que operaban asi como el octal
# python2   03  anteponiendo un cero
# en python3 la funcion oct devuelve un str que lo representa

# Nota.- tambien se puede escribir de modo hexadecimal

print("\nnumero hexadecimal (se guarda como int)")
hexadecimal=0x23
print(hexadecimal)
print(type(hexadecimal))

#Nota,. tambien se pueden escribir valores binarios 
print("\nnumero binario, (se guarda como int)")
binario=0b111100111
print(binario)
print(type(binario))

# numeros tipo float
# se utiliza el estandar IEEE 754 
# para 64 bits 1bit signo  11 exponente 52 para la mantisa
# rango aprox: +-2.22*10^-308 hasta +-1.79+*10^308

print("\nnumero de coma flotante")
numerofloat=2.12345
print(numerofloat)
print(type(numerofloat))

#otro tipo de numero que existe son los de tipo complejo
#se expresan solo como una suma de valores numero+numeroj 
#en memoria se guarda como dos archivos tipo double

print("\nnumero complejo")
complejo=122+2.22j
print(complejo)
print(type(complejo))






