#Coding: UTF8

x=float(input("Escriba el valor limite: "))
i=0
suma=0

while x<=0:
	print "El limite debe ser mayor que 0. Intentelo de nuevo."
	x=float(input("Escriba el valor limite: "))

while (suma<x):
	aux=float(input("Introduzca un nuevo numero: "))
	suma=aux+suma
	print "Ha superado el limite. La suma de los numeros introducidos es ",suma,"."
	print "Programa finalizado"

