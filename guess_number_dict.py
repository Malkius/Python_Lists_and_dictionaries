import json
import random
import datetime
import locale

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES')
fecha = datetime.datetime.now()
# Formato 24 hr
fecha.strftime("%A %d de %B del %Y - %H:%M")

# PRESENTACIÓN Y NOMBRE DE JUGADOR #
nombre = input("Hola jugador, ¿cuál es su nombre? ")
print("Encantado " + nombre + ". Trate de adivinar mi número del 1 al 20")

secreto = random.randint(1, 20)
intentos = 0

# LLAMAMOS AL TXT DONDE GUARDAMOS MARCADORES #
with open("hall_of_fame_dict.txt", "r") as archivo_puntuaciones:
    top_marcadores = json.loads(archivo_puntuaciones.read())
    print("Top de Rappeles: " + str(top_marcadores))

# ORDENACIÓN DE LOS 3 MEJORES INTENTOS #
archivo_puntuaciones_ord = sorted(top_marcadores, key=lambda x: x["intentos"])[:3]

for marcador_top3 in top_marcadores:
    texto_top3 = "Jugador {0} tiene {1} intentos el {2}.\n EL número era: {3} y los errores: {4}".\
        format(marcador_top3.get("nombre"), str(marcador_top3.get("intentos")),
               marcador_top3.get("fecha"), marcador_top3.get("pregunta"), marcador_top3.get("errores"))
    print(texto_top3)
errores = []

while True:
    pregunta = int(input("Qué número estoy pensando?: "))
    intentos += 1

    if pregunta == secreto:
        top_marcadores.append({"Nombre": nombre, "Intentos": intentos,
                               "Fecha": str(fecha.strftime("%A %d de %B del %Y - %H:%M")),
                               "Número": pregunta, "Fallos": errores})

        with open("hall_of_fame_dict.txt", "w") as archivo_puntuaciones:
            archivo_puntuaciones.write(json.dumps(top_marcadores))

        print("Enhorabuena " + nombre + ", o quizás, Octavio Aceves, lo ha logrado en: " + str(intentos) + " intentos")
        seguir = input("¿Quiere seguir jugando? (s/n): ").lower()
        if seguir == "s":
            print("Muy bien, probemos otra vez.")
            secreto = random.randint(1, 20)
            intentos = 0
        else:
            print("Hasta la vista.")
            break
    # SI NO ACIERTA, IMPRIME SI ES MAYOR O MENOR #
    elif pregunta < secreto:
        print("Ups, mi número es mayor")
    elif pregunta > secreto:
        print("Ups, mi número es menor")

    errores.append(pregunta)
