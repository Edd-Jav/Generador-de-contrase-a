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
    