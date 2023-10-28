#1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es.
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
def verify_dni(dni):
    if len(dni) == 7 or len(dni) ==8:
        return True
    else:
        return False
#2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. 
# Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro.
def last_word(phrase):
    trimmed_phrase = phrase.split()
    return trimmed_phrase[-1]
#3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
# Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso
#de un nombre vacio.
#Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: 
# nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
#Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar
# al usuario en un bucle hasta que ingrese un DNI correcto.
#Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de
# letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
#Nombre: María Ines Rosales
#DNI: 25469648
#ID -> Maria7254

def obtain_id():
    while True:
        name = input("Enter your name:")
        if name=="":
            break
        name = name.split(", ")
        while True:
            dni = input("Please enter your dni: ")
            if verify_dni(dni):
                break
            print("Please enter a valid DNI")
        if len(name) == 2:
            first_name = name[0]
            last_name = name[1]
        elif len(name) == 3:
            first_name = name[0]
            second_name = name[1]
            last_name = name[2]
        else:
            print("Please enter a valid format")
            continue
        id = first_name +  str(len(last_name)) + dni[0:3]
        break
    return(id)

#4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def is_multiple(num1,num2):
    if(num1%num2 == 0):
        return True
    return False

def get_multiple():
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))
    if is_multiple(num1,num2):
        print(f"{num2} is a multiple of {num1}")
    elif is_multiple(num2,num1):
        print(f"{num1} is multiple of {num2}")
    else:
        print("None of the entered numbers is a multiple of the other.")

#5.Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima
# de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

def get_medium_temperature(max, min):
    return (max + min) / 2

#6.Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional 
#tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “.
# Crea un programa principal donde se use dicha función.
def make_aesthetic(text):
    new_text = ''
    for i in text:
        new_text = new_text + i + " "
    return new_text
#7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
def return_max_and_min(nums):
    max = 0
    min = 0
    for index, i in enumerate(nums):
        print(index)
        if index == 0:
            max = i 
            min = i
        elif i > max:
            max = i
        elif i < min:
            min = i
    return max,min

    