# Evidencia 1, Estructura de datos y su procesamiento.

from collections import namedtuple
from datetime import datetime

def checarFecha(fecha):
    dia = fecha[0:2]
    mes = fecha[3:5]
    anio = fecha[6:10]
    fechaNuvoFormato = anio + "-" + mes + "-" + dia
    return fechaNuvoFormato

Venta = namedtuple('Ventas', ('descripcion', 'cantidadVenta', 'precioVenta', 'fechaVenta'))
DiccionarioVentas = {}
ListaVentas = []
separador = ('-' * 45)
subtotal = 0

print('Bienvenido(a) al negocio de ventas de computo')
print(separador)

def Menu():
    opcion = int(input('\nMenú de opciones:\n[1] Registrar una venta\n[2] Consultar una venta\n[3] Consultar ventas de una fecha \n[4] Salir\n» '))
    return opcion

def RegistrarVenta():
    ListaVentas=[] # Limpieza de la lista
    print('\n--------- Registro de venta ---------')
    while True:
        folio = int(input(f'Introduzca folio de venta de el equipo(s)\n» '))
        if folio in DiccionarioVentas.keys():
            print('Error, ya existe una venta con ese folio de venta')
        else:
            break
    while True:
        Nombre_Cliente = input('Introduzca Nombre del Cliente\n» ')
        fechaVenta = input('Introduzca Fecha de Venta\n» ')
        descripcion = input('Introduzca descripción del tipo de el Equipo \n» ')
        cantidadVenta = int(input('Introduzca cantidad a vender del tipo de el Equipo mencionado\n» '))
        precioVenta = int(input('Introduzca precio (sin iva) del tipo de Equipo (por unidad)\n» $'))
        print(separador)
        subtotal = (cantidadVenta * precioVenta)
        print(f'Subtotal (sin iva) de los Equipo (s) tipo {descripcion}:','${:.2f}'.format(subtotal))
        print(separador)
        fechaVenta = datetime.strptime(fechaVenta, "%d/%m/%Y").date()
        organizacionVenta = Venta(descripcion,cantidadVenta, precioVenta, fechaVenta)
        ListaVentas.append(organizacionVenta)
        DiccionarioVentas[folio] = ListaVentas
        agregaOtraLlantaMismaVenta = int(input('¿Desea agregar otra(s) venta(s) de Equipo(s) a la misma venta?\n[1] Si \n[2] No\n» '))
        if agregaOtraLlantaMismaVenta == 2:
            dimensionVentas, acumuladoVentas = 0 , 0
            while dimensionVentas < len(DiccionarioVentas[folio]):
                aculumador = (int(DiccionarioVentas[folio][dimensionVentas].precioVenta) * int(DiccionarioVentas[folio][dimensionVentas].cantidadVenta))
                acumuladoVentas =  aculumador + acumuladoVentas
                dimensionVentas += 1
            print(separador)
            print('Subtotal: ${:.2f}'.format(acumuladoVentas),'\nIVA:','${:.2f}'.format(acumuladoVentas * .16))
            print('-' * 16,'\n\nTotal: ${:.2f}'.format(acumuladoVentas*1.16, 2),f'\nVenta realizada el: {fechaVenta}\n')
            print(separador)
            break

def ConsultarVenta():
    consulta = int(input('Folio a consultar: '))
    dimension, totalVentas = 0 , 0
    if consulta in DiccionarioVentas.keys():
        while dimension < len(DiccionarioVentas[consulta]):
            print(separador)
            print(f'Descripción del tipo de Equipo o Producto: {DiccionarioVentas[consulta][dimension].descripcion}')
            print(f'Cantidad de Equipo: {DiccionarioVentas[consulta][dimension].cantidadVenta}')
            print('Precio: ${:.2f}'.format(DiccionarioVentas[consulta][dimension].precioVenta, 2))
            print(f'Fecha: {DiccionarioVentas[consulta][dimension].fechaVenta}')
            totalVentas = (int(DiccionarioVentas[consulta][dimension].precioVenta) * int(DiccionarioVentas[consulta][dimension].cantidadVenta)) + totalVentas
            dimension += 1
        print(separador)
        print('Subtotal: ${:.2f}'.format(totalVentas),'\nIVA:','${:.2f}'.format(totalVentas * .16))
        print('-' * 16,'\n\nTotal: ${:.2f}\n'.format(totalVentas + totalVentas * .16, 2))
        print(separador)
    else:
        print('La clave no esta registrada')

def VentaFecha():
    print("\nIngrese una fecha para buscar todas las ventas de esta")
    print(f'¡Porfavir digite la fecha en el siguiente formato! (Dia/Mes/Año)')
    print(f'Ejemplo: 23/07/2020')
    
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    for venta, datos in DiccionarioVentas.items():
        print(f'{datos[0]}')

    fec = input("Fecha: ")

    fecFormat = checarFecha(fec)
    print(fecFormat)
    SavePoint = 0
    dataVentas = len(DiccionarioVentas)
    print(f'\n{"*"*50}')
    print(f'Folio,Fecha,Descripción,Cantidad,Total')
    for venta, datos in DiccionarioVentas.items():
        if str(datos[0][3]) == str(fecFormat):
            print(f'{venta}, {datos[0][3]}, {datos[0][0]}, {datos[0][1]}, {datos[0][2]}')
        else:
            SavePoint +=1
            if SavePoint == dataVentas:
                print(f'{"*"*50}')  
                print(f'\nNINGUNA VENTA ENCONTRADA CON ESA FECHA\n')
                print(f'FAVOR DE VERIFICAR QUE: {fecFormat} ESTE CORRECTO')
while True:
    opcionElegida = Menu()
    if opcionElegida == 1:
        RegistrarVenta()
    if opcionElegida == 2:
        ConsultarVenta()
    if opcionElegida == 3:
        VentaFecha()
    if opcionElegida == 4:
        break