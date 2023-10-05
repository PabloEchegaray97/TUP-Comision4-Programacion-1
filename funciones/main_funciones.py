from lab1 import verify_dni, last_word, obtain_id, get_multiple, get_medium_temperature, make_aesthetic, return_max_and_min
"""
#1 
print(verify_dni('12345678'))
#2
print(last_word("    :D Hi my name is Pablo    "))
#3
obtain_id()
#4
print(get_multiple())
#5
dias = int(input("Ingrese la cantidad de dias:"))
max = 0
min = 0
for i in range(1, dias+1):
    min = int(input("Ingrese la temperatura mínima:"))
    max = int(input("Ingrese la temperatura máxima:"))
    print(f"La media para el dia {i} fue de {get_medium_temperature(min,max)} °C")
#6

"""
print(make_aesthetic("Hola Pablito chikito"))
#7
nums = [1,2,3,4,5,6,7,102313,3,4,2,6,1,2,13192312039123.03]
a,b = return_max_and_min(nums)
print(f"minimo:{b}, maximo:{a}")