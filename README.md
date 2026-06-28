# Generador-de-contrase-a
Nombre: Edwin Javier Moreta Peralta
Objetivo: Diseñar e implementar un programa informático funcional en el lenguaje de programación Python que automatice la generación de contraseñas aleatorias y seguras, aplicando los conceptos fundamentales de la lógica de programación y la modularidad adquiridos durante el semestre académico.
Funcionalidad: El sistema sigue un flujo lógico secuencial que puede describirse en los siguientes pasos:
El programa muestra un mensaje de bienvenida al usuario.
•	Solicita al usuario que ingrese el número de caracteres deseado para la contraseña.
•	Convierte la entrada a tipo entero y la almacena en numero_caracteres.
•	Evalúa si numero_caracteres es menor que 8; en ese caso, lanza un error y detiene la ejecución.
•	Si el valor es válido, llama a crear_contraseña() con la longitud y la lista de funciones.
•	Dentro del bucle, selecciona aleatoriamente una de las cuatro funciones generadoras y la ejecuta.
•	Concatena el carácter retornado a la cadena contraseña.
•	Repite los pasos 6-7 hasta completar la longitud solicitada.
•	Retorna la contraseña completa y la muestra al usuario mediante un mensaje formateado.
Fecha: 28 de junio del 2026


import random
#letras minusculas
#letras mayusculas
#simbolos

print("<>---<>---<>---<>---<>---<>---<>---<>---<>")
print("  Bienvenido al generador de contraseñas ")
print("<>---<>---<>---<>---<>---<>---<>---<>---<>")
print("\n")

numero_caracteres = int(input("Numero de caracteres para tu contraseña?(8 o mas): "))
def crear_numero():
    return str(random.randint(0, 9))

def crear_letra_mayuscula():
 letras_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 i = random.randint(0, (len(letras_mayusculas) -1))
 return letras_mayusculas[i]

def crear_letra_minuscula():
 letra_minuscula = "abcdefghijklmnopqrstuvwxyz"
 i = random.randint(0, (len(letra_minuscula) -1))
 return letra_minuscula[i]

def crear_simbolo():
 simbolo = ",.-_+ç¡!$%&/()"
 i = random.randint(0, (len(simbolo) -1))
 return simbolo[i]


funcion_crear_contraseña = [crear_numero, crear_letra_mayuscula, crear_letra_minuscula, crear_simbolo]
def crear_contraseña(char_length, funciones):
    contraseña = ""
    for caracter in range(char_length):
        rand_index = random.randint(0, (len(funciones) - 1))
        llamar_funcion = funciones[rand_index]()
        caracter = llamar_funcion
        contraseña += caracter
    return contraseña
if numero_caracteres < 8:
    raise ValueError("El numero de caracteres debe ser 8 o mas")
else:
    contraseña = crear_contraseña(numero_caracteres, funcion_crear_contraseña)
    print(f"\nTu contraseña es: {contraseña}")
    
