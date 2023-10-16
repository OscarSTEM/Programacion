import random
#Recopila la información de tres Zombies: Su color, su longitud de salto y su frecuencia de salto.
#¿Que zombie ganaria una carrera de 50 metros? ¿Y de 100 metros?
#[Crea una funcion a la que le pases los metros que tenga la carrera y las características de los zombies y te devuelva quién gana]
#Esa funcion seria muy compleja y cambiaría dependiendo del número de zombies que participaran en la carrera: 
#Crea una funcion a la que le pases la info de un solo zombie y te indique en qué segundo llegaría cada uno de los zombiens a la meta. 
#Al comparar los segundos que tarda cada uno de los zombies podremos saber cuál es el ganador.
# Info sobre el zombie.
#...
#El Zombie Rojo tarda 30 segundos.
#El Zombie Azul tarda 27 segundos.
#El Zombie Verde tarda 33 segundos.

#Gana el Zombie Azul.
#Funcion
def pedirColor():
    color = input("Dime el color del zombie: ")
    return color
def longitudSalto():
    longitud = int(input("Dime la longitud de salto: "))
    return longitud
def frecuenciaSalto():
    frecuencia = int(input("Dime la longitud: "))
    return frecuencia 
#Codigo Principal
minMetros = 50
maxMetros = 100
tiempoTotal = 0

zombieColor = pedirColor()
longitudZombie1 = longitudSalto()
frecuenciaSaltoZombie1 = frecuenciaSalto()

print(f"El primer participante es un zombie de color {zombieColor},la longitud de salto que ha sido un {longitudZombie1}\ny de ultimas  la frecuencia con la que ha sido {frecuenciaSaltoZombie1}")
print(f"El segundo participante es un zombie de color {zombieColor},la longitud de salto que ha sido un {longitudZombie1}\ny de ultimas  la frecuencia con la que ha sido {frecuenciaSaltoZombie1}")
while minMetros >0:
    tiempoTotal += frecuenciaSaltoZombie1
    minMetros -= longitudZombie1
    print (f"El zombie de color {zombieColor} ha tardado {tiempoTotal} segundos en llegar a la meta: ")
    