# El input recoge el dato y lo guarda en nombre.
print ("Introduce tu nombre: ")
nombre = input()
print ("Hola " + nombre)
# Existen 2 tipos de =s en programacion
# = -> Asigna lo que hay a la izq
# lo que hay en la derch
# Ej. numero = 5
# Ej. == ->Es un igual LÓGICO, es decir compara
#                    los valores que tiene a izq y derch.
#                   Devuelve true, si son iguales; o false, si son distintas
# 1. Entrada: Numero. Salida: True si es mayor de edad
# Input siempre guarda el valor introducido como str. Si queremos que sea un
# entero hay que transformarlo. int(input)...))
edad = int(input ("Introduce tu edad: "))
#Para saber el tipo -> print (type (numero))
print ("¿Es mayor de edad?: ")
# Se puede escribir 'esMayorEdad = edad >= 18'
esMayorEdad = ( edad >=18 )
print (esMayorEdad)
#esMayorEdad es de tipo bool.
print (type (esMayorEdad) )
if esMayorEdad:
    print ("Es mayor de edad")
else:
     print ("Es menor de edad")
print ("se imprime siempre")
if edad >= 18:
    print ("Es mayor de edad")
else:
     print ("Es menor de edad")
print ("se imprime siempre")
# Sin la variable booleana EsMayorEdad

# El int lo que hace es transformar a un numero
# 3. Entrada: Numero. Salida: True si es positivo
numero = int(input ("Introduce un numero: ") ) 
print ("¿Es numero positivo?: " )
esPositivo = (numero > 0)
if esPositivo:
    print ( "Es positivo" )
elif numero == 0:
    print ( "Es 0" )
else :
    print ( "Es negativo" )
# 4. Entrada: Letra. Salida: True si es vocal
letra = input ("Introduce una letra: " ) 
print ("¿Es vocal?: " )
print (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" )
# 5. Entrada: Numero. Salida: True si está aprobado
nota = int(input ("Cual es tu nota: ") )

if nota  <5 :  
    print ("Insuficiente" )
elif nota <6 :
    print ("Suficiente")
elif nota  <7 :
    print ("Bien")
elif nota <9 :
    print ("Notable")
elif nota <=10 :
    print ("Sobresaliente")
#Si asumimos nota valida:
#' if nota <= 10 and nota >= 9:'
# if nota <= 10 and nota >= 9:

# print ("Sobresaliente")
#elif nota >= 7:
# print ("Notable")
#elif nota >=6:
#print ("Bien")
#elif nota >=5:
#print no("Suficiente")
#elif nota >=4:
#print ("Insuficiente")


