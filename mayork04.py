#Coding: UTF8

x=input("Escriba la cantidad de numeros positivos a solicitar: ")
i=0
j=0

while (i<x):
	aux=input("Introduzca un nuevo numero: ")
	j+=1
	if aux>0:
		i+=1
		
print "Has escrito",j,"numeros",",",i,"de ellos positivos."
print "Programa finalizado"
