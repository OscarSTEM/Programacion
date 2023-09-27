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
numero = int(input ("Introduce tu edad: "))
#Para saber el tipo -> print (type (numero))
print ("¿Es mayor de edad?: ") 
print (numero >= 18)
# El int lo que hace es transformar a un numero
# 2. Entrada: Día semana. Salida: True si fin de semana
diaSemana = input ("Introduce un dia de la semana: " ) 
print ("¿Es fin de semana?: ")
print ( diaSemana == "sabado" or diaSemana == "domingo" )
# 3. Entrada: Numero. Salida: True si es positivo
numero = int(input ("Introduce un numero: ") ) 
print ("¿Es numero positivo?: " )
print (numero >=0)
# 4. Entrada: Letra. Salida: True si es vocal
letra = input ("Introduce una letra: " ) 
print ("¿Es vocal?: " )
print (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" )
# 5. Entrada: Numero. Salida: True si está aprobado
numero = int(input ("numero >=5 and 10: " ))
print ("¿Esta aprobado?: " )
print (numero >=5 and numero <=10)
