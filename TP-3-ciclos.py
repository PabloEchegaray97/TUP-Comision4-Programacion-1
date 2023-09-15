#1) 1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Ingrese una palabra y esta se repetira 10 veces despues de ser ingresada:")
for i in range(10):
    print(palabra)

#2) 2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input("Ingrese su edad:"))
for i in range(edad):
    print("Cumpliste: ", i+1)

#3) 3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
while True:
    numero = int(input("Ingrese un numero entero positivo:"))
    if numero<0:
        print("El numero ingresado no es positivo")
    else: 
        print(f"Los numeros impares de 1 hasta {numero} son:")
        for i in range(1, numero+1):
            if i%2 !=0:
                if i==numero:
                    print(i, end=".")
                else:
                    print(i, end=", ")
        break
# 4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
while True:
    numero2 = int(input("Ingrese un numero: "))
    if numero2<0:
        print("El numero ingresado no es positivo")
    else: 
        print(f"Cuenta regresiva desde {numero2} hasta 0:")
        for i in reversed(range(numero2+1)):
            if numero2==0:
                print(i)
            else:
                print(i, end=", ")
        break
# 5- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
cantidad_inversion = int(input("Ingrese la cantidad que desea invertir: "))
interes = int(input("Ingrese el interés anual: "))
tiempo =  int(input("Ingrese la cantidad de años: "))
capital_acumulado = cantidad_inversion
for i in range(1, tiempo+1):
    nuevo_interes = (capital_acumulado*interes)/100
    print("EL INTERES ES:", nuevo_interes)
    capital_acumulado = capital_acumulado + nuevo_interes
    print(f"Año {i}:\nCapital invertido:{cantidad_inversion}\nCapital invertido mas intereses: {capital_acumulado}")
#6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
altura = int(input("Ingrese la altura del triangulo"))
for i in range(1,altura+1):
    for j in range(i):
        print("*", end="")
    print()
#7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
for i in range (1,11):
    print(f"Tabla del {i}:")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
#8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
num = int(input("Enter an integer"))
value=1
for i in range(1, num+1):
    row_value=value

    for j in range(i):
        print(row_value, end=" ")
        row_value-=2

    print()
    value+=2
#9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
password = 'secret'

while True:
    input_pass = input('Hi! Please enter your password:')
    if (input_pass == password):
        print('The password is correct.')
        break
    print('Password incorrect')
#10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
num = int(input("Ingrese un numero: "))
counter = 0
for i in range(1, num+1):
    if num%i == 0:
        counter+=1
if(counter>2):
    print("El numero no es primo")
else:
    print("El numero es primo")

#11-Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
word = input("Enter a word: ")

print(f"The letters of {word} one by one in order desc is: ")
for i in reversed(word):
    print(i)

#12-Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
phrase = input("Enter a phrase please: ")
letter = input("Now, enter a letter: ")
counter = 0
for i in phrase:
    if i==letter:
        counter+=1
print(f"The number of times that '{letter}' appears is: {counter}")

#13-Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
phrase=''
while phrase!="salir":
    phrase = input('Enter a word and watch the echo ! (Enter "salir" if you want to exit) Word: ')
    if(phrase=='salir'):
        break
    print(phrase)

#14-Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
print('Enter two numbers, then you will see witch numbers are odd between them:')
while True:
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    aux = 0
    if(num1 == num2) and num1%2==0:
        print('You entered the same number twice and its odd')
        break
    elif num1==num2:
        print('You entered the same number twice and its even')
        break
    else:
        if num1>num2:
            aux = num2
            num2 = num1
            num1 = aux 
        for i in range(num1, num2 + 1):
            if(i%2 == 0):
                print(f"The number {i} is odd")
            else:
                print(f"The number {i} is even")
    break

#15 - Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

num = int(input("Please enter an int number greater than 0: "))
for i in range(1, num + 1):
    if(num%i == 0):
        print(f"{i} es divisor de {num}")

#16 - Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

num = int(input("Enter how many numbers are going to be input by keyboard"))
for i in range(1, num +1):
    i = int(input("Enter a number:"))
    if(i<0):
        print("The number is negative")
    
#17 - Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
phrase=str(input("Escriba una frase: "))
phrase=phrase.upper()
vowels=[]

for letter in phrase:
    if letter in "AEIOU" and letter not in vowels:
        vowels.append(letter)

print(f"Las vocales en la frase son: {vowels}")
#18 - Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
fibo=[0,1]

for i in range(2,10):
    next_num=fibo[i-1]+fibo[i-2]
    fibo.append(next_num)

for num in fibo:
    print(num)

#19 - Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.
amount=float(input("Ingrese la cantidad que desea ahorrar: $"))

if amount<0:
    print("¡ERROR! Ingrese una cantidad válida (positiva)")
else:
    saving=0

    while saving<amount:
        new_saving=float(input("Ingrese el monto que desea ingresar: $"))

        if new_saving<0:
            print("¡ERROR! Ingese una cantidad válida (positiva)")
        else:
            saving+=new_saving
            remaining=amount-saving
            print(f"Usted ha ahorrado ${saving}, le fantan {remaining} para alcanzar su objetivo de {amount}")
    
    if saving==amount:
        print(f"Usted ha alcanzado su objetivo de ahorrar ${amount}")
    else:
        additional=saving-amount
        print(f"Usted ha alcanzado su objetivo de ahorrar ${amount} y ha obtenido un adicional de {additional}")

#20 - Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
num=1
addition=0
while num!=0:
    num=int(input("Ingrese un número entero positivo: "))
    if num<0:
        print("¡ERROR! Ingrese solo números enteros positivos")
    else:
        addition=addition+num
print(f"La suma de todos los números válidos ingresados es {addition}")

#21 - Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
num=1
highest=0

while num!=0:
    num=int(input("Ingrese un número entero positivo: "))
    if num<0:
        print("¡ERROR! Ingrese solo números enteros positivos")
    else:
        if num>highest:
            highest=num
print(f"El mayor número ingresado fue {highest}")
#22 - Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
num=0
even_number=0

while num!=-1:
    num=int(input("Ingrese un número entero positivo (o -1 para salir): "))

    if num==-1:
        break
    elif num<0:
        print("¡ERROR! Ingrese un número válido (positivo)")
    else:
        num_str=str(num)
        addition=0

        for digit_str in num_str:
            digit=int(digit_str)
            addition+=digit
        
        print(f"La suma de los dígitos de {num} es {addition}")

        if num%2==0:
            even_number+=1

print(f"Total de números pares ingresados: {even_number}")
#23 - Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
#24 - Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
product=1
total=0

while product!=0:
    product=float(input("Ingrese el valor del productor: "))
    if product<0:
        print("¡ERROR! Ingrese solo montos válidos")
    else:
        total=total+product

if total>1000:
    discount=total*0.1
    final_price=total-discount
    print(f"El total de su compra es de ${total}")
    print(f"Se le aplicó un descuento del 10%, así que el precio final es de {final_price}")
else:
    print(f"El total de su compra es de ${total}")

#25 - Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1
num=int(input("Ingrese un número entero positivo: "))

if num<0:
    print("¡ERROR! El número debe ser positivo")
elif num==0:
    print("El factorial de 0 es 1")
else:
    factorial=1

    for i in range(1, num+1):
        factorial*=i
    
    print(f"El factorial de {num} es {factorial}")