import random
import json

# SOLICITUD NOMBRE DEL JUGADOR Y PERMISO PARA EMPEZAR A JUGAR #
nombre = input("Hola jugador, ¿cuál es tu nombre? ")
print("Encantado de conocerte " + nombre)
permiso = input("¿Eres capaz de adivinar el número que estoy pensando(s/n)? ").lower()
if permiso == "s":
    print("Muy bien " + nombre + ", empecemos")
else:
    print("De acuerdo " + nombre + " vuelve cuando quieras")
    exit()

# LLAMADA A FICHERO TXT CON INTENTOS REALIZADOS #
with open("hall_of_fame.txt", "r") as archivo_marcador:
    top_lista = json.loads(archivo_marcador.read())
    print("Top de Rappeles: " + str(top_lista))

# GENERA NÚMERO RANDOM Y PONE INTENTOS A 0 #
secreto = random.randint(1, 20)
intentos = 0

while True:
    # PREGUNTA AL USUARIO POR EL NÚMERO RANDOM #
    adivina = int(input("Dime un número del 1 al 20: "))
    intentos += 1
    # SI ACIERTA, GUARDA EL NÚMERO DE INTENTOS EN TXT E IMPRIME MENSAJE #
    if adivina == secreto:
        top_lista.append(intentos)

        with open("hall_of_fame.txt", "w") as archivo_marcador:
            archivo_marcador.write(json.dumps(top_lista))

        print("Caray , " + str(secreto) + " es mi número " + nombre + ", tienes madera de Rappel")
        print("Lo has logrado en " + str(intentos) + " intentos")

        # PREGUNTA VOLVER A JUGAR Y EN CASO DE SÍ, GENERA UN NUEVO RANDOM Y Nº DE INTENTOS #
        seguir = input("¿Quieres seguir jugando " + nombre + " (s/n)?").lower()
        if seguir == "s":
            print("Muy bien")
            secreto = random.randint(1, 20)
            intentos = 0
        else:
            print("Hasta la vista")
            break

    # SI NO ACIERTA, IMPRIME SI ES MAYOR O MENOR #
    elif adivina < secreto:
        print("Ups, mi número es mayor")
    elif adivina > secreto:
        print("Ups, mi número es menor")
