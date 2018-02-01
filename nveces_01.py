#Coding: UTF8

x=input("Introduzca un numero: ")
i=0
suma=0

while (i<x):
	aux=input("Introduzca un nuevo numero: ")
	if aux>0:
		i+=1
		suma=aux+suma
print suma
print "Programa finalizado"
