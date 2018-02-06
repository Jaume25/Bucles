#Coding: UTF8

x=int(input("Escriba un numero: "))
y=int(input("Escriba un numero mayor que "+str(x)+": "))
z=int(input("Escriba un numero entre "+str(x)+" y "+str(y)+": "))
cont=0

while z>x and z<y:
	z=int(input("Escriba un numero entre "+str(x)+" y "+str(y)+": "))
	cont+=1
print "Programa terminado"
print "Ha escrito "+str(cont)+" numeros entre "+str(x)+" y "+str(y)+"."
