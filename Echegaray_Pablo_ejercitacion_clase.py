print('Ingrese a continuación la fecha con el formato solicitado:')
fecha_input = input('Formato: [Día de la semana], [DD/MM]: ')

parts = fecha_input.split(', ')
print("Parts:", parts)
dia_semana = parts[0].lower()
dia, mes = map(int, parts[1].split('/'))
print("Día de la semana:", dia_semana)  
print("Día:", dia)
print("Mes:", mes)

if dia_semana == 'l' or dia_semana =='m' or dia_semana=='x' or dia_semana=='j' or dia_semana=='v':
    if dia <= 0 or dia > 31:
        print('El dia ingresado no es valido')
        quit()
    elif mes <= 0 or mes > 12:
        print('El mes ingresado no es valido')
        quit()
    elif dia > 29 and mes == 2:
        print('La fecha es invalida')
        quit()
    elif dia>30 and (mes==4 or mes==6 or mes==9 or mes == 11):
        print('La fecha es invalida')
        quit()
    elif len(dia_semana)>1:
        print('El dia de la semana ingresado es invalido')
        quit()

cantidad_aprobados = 0
cantidad_desaprobados = 0
if (dia_semana == 'j' or dia_semana =='v'):
    decision = '2'
else: 
    print(f'¿El dia ({dia}/{mes}) se tomaron examenes?')
    print(f'1.Si\n2.No')
    decision = input()
if decision=='1':
    if dia_semana=='l':
        print(f'En el dia lunes se tomaron examenes al nivel inicial')
        cantidad_aprobados = int(input('Ingrese la cantidad de aprobados'))
        cantidad_desaprobados = int(input('Ingrese la cantidad de desaprobados'))
        total = cantidad_aprobados + cantidad_desaprobados
        print(f'El porcentaje de alumnos aprobados es de: {(cantidad_aprobados/total)*100}%')
    elif dia_semana=='m':
        print(f'En el dia martes se tomaron examenes al nivel intermedio')
        cantidad_aprobados = int(input('Ingrese la cantidad de aprobados: '))
        cantidad_desaprobados = int(input('Ingrese la cantidad de desaprobados'))
        total = cantidad_aprobados + cantidad_desaprobados
        print(f'El porcentaje de alumnos aprobados es de: {(cantidad_aprobados/total)*100}%')
    elif dia_semana=='x':
        print(f'En el dia miercoles se tomaron examenes al nivel avanzado')
        cantidad_aprobados = int(input('Ingrese la cantidad de aprobados'))
        cantidad_desaprobados = int(input('Ingrese la cantidad de desaprobados'))
        total = cantidad_aprobados + cantidad_desaprobados
        print(f'El porcentaje de alumnos aprobados es de: {(cantidad_aprobados/total)*100}%')
elif decision=='2':
    if dia_semana =='j':
        print('El dia jueves corresponde a practicas habladas')
        porc_asistencia = int(input('Ingrese el porcentaje de asistencia: '))
        if porc_asistencia > 100 or porc_asistencia < 0:
            print('El porcentaje indicado no es valido')
            quit()
        elif porc_asistencia > 50:
            print('Asistió la mayoria de alumnos a la practica hablada')
        else: 
            print('No asistio la mayoria de alumnos a la practica hablada')
    elif dia_semana=='v':
        if (dia==1 and mes==1) or (dia==1 and mes==7):
            print('Comienzo de nuevo ciclo')
            cant_alumnos = int(input('Ingrese la cantidad de alumnos del nuevo ciclo: '))
            arancel = int(input('Ingrese el arancel correspondiente a cada alumno: $ '))
            print(f'El ingreso total es de ${arancel*cant_alumnos}')
    else:
        print('No hay datos que proporcionar')

