# Funciones
# num1, num2, num3 son argumentos de entrada.
def mediaTresNumeros (num1,num2,num3):
    resultado = (num1+num2+num3)/3
    # Nunca' en una función: print (resultado)
    return resultado
# 'resultado' es el argumento de salida
# Se utiliza esta para operaciones sencillas (otraMediaTresNumeros)
def otraMediaTresNumeros (num1,num2,num3):
    return (num1,num2,num3)/3
# Para dividir la operacion final es más sencilla:
def otraOtraMediaTresNumeros (num1,num2,num3):
    suma = num1+num2+num3
    return suma/3
# Podemos tener funciones sin return
# Esto es una excepción, de normal no usamos
#   print () en funciones, solo cuando el objetivo
#   de la funcion sea mostrar algo.
def dibujarLinea(forma): # forma = "="
    print (forma*20)
def dibujarLineaPuntos():# sin parametros de entrada
    print ("."*20)
# sin return
# Para hacerlo sin print ():
def crearLinea (forma):
    return forma*20
def otraDibujarLinea (forma):
    print (forma*20)
def otraOtraOtraMediaTresNumeros (num1,num2,num3):
    suma = num1+num2+num3
    return suma/3
def cuentaNumero (num1,num2,num3) :
    resta = num1-num2-num3
    return resta/2
def otraOtraDibujarLinea (forma):
    print (forma*20)
def presentacion (nombre,edad):
    return "Hola, me llamo Oscar y tengo 25"
    
#----------------------------------------------------------------------
# Codigo principal - MAIN
print ("Probando funcion")
media = mediaTresNumeros (20,30,40) 
print (media)
dibujarLinea ("=")
dibujarLinea ("x")
dibujarLinea ("_")
dibujarLineaPuntos ()
# print () de lo que devuelve la funcion. ->
# Para no hacer print dentro de la función
print (crearLinea ("*"))
#Linea hecha con oooooooooooooooooooo
#Escribir por pantalla la media de 5,10 y 15: 10"
#00000000000000000000
otraDibujarLinea ("o")
print (otraOtraOtraMediaTresNumeros(10,15,20))
otraOtraDibujarLinea("0")
print (cuentaNumero(40,30,60))
nombre = input ("Escribe tu nombre: ")
edad = input ("Escribe tu edad:")
print (presentacion (nombre,edad))

