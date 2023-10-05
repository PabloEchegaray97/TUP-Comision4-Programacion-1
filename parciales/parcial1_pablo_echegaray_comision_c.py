
#Realizar un programa que cumpla con las siguientes condiciones:

#Pedir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
#Generar un menú de opciones, que serán:
#Juego de números.
#Juego de palabras.
#Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros (condición de salida: cuando ingrese 0). Al finalizar mostrar por pantalla:
#El mayor número par.
#El promedio de los números impares.
#Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y mostrar por pantalla la cantidad de cada vocal que contiene dicha frase.
#No olvides realizar las debidas validaciones!


name = input("Please enter your name: ")
print(f"Hi {name}, please select an option:")
print("1.Number's game\n2.Word's game\nOther: Exit")
option = int(input("Option: "))
greater_even = 0  # Mayor número par ingresado
average = 0       # Promedio de números impares ingresados
counter = 0       # Contador para números impares
numbers = []      # Lista para almacenar números
phrase = ""       # Frase para ser ingresada por el usuario
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}  # Diccionario para contar vocales

# Comprobar la opción seleccionada
if option == 1:
    # Juego de números
    while True:
        number = int(input(f"Enter a number please: "))
        if number==0:
            print("Execution interrupted")
            break
        
        numbers.append(number) # Agregar número a la lista
    print(numbers) # Mostrar la lista de números ingresados
    for i in numbers:
        if i>greater_even and i%2==0: #Si i es mayor que el par mayor y si es par, se reemplaza por i
            greater_even = i
        elif i%2!=0: #Sino si i no es par, se suma uno al contador y se guarda la suma
            counter += 1
            average = average + i
    if counter !=0: #Si el contador no es igual a 0, hacer la division
        average = average / counter 
    print(f"The greater and even is: {greater_even}\nThe average of odd numbers entered are: {average}")

elif option == 2:
    # Juego de palabras
    print(f"{name}, please enter a phrase: ")
    phrase = input()
    print(f"The phrase is: \n``{phrase}´´")
    phrase = phrase.lower() # Para evitar errores de comparacion se transforma a minusculas.
    for vowel in vowels: #Recorre cada vocal de la lista de vocales, luego cada letra en la frase, si esta la vocal en esa frase cambia su valor en el diccionario
        for letter in phrase:
            if vowel == letter:
                counter +=1
        vowels[vowel] = counter
        counter = 0
    print(f"The number of vowels in your phrase are: {vowels}")
print(f"{name}, thank you for playing ! :)")