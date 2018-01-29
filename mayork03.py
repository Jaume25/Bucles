#coding: utf-8

num1=int(input("Escriba un numero: "))
num2=int(input("Escriba un numero mayor: "))


while (num1<num2):
	num1=num2	
	num2=int(input("Escriba un numero mayor que "+str(num1)+": "))	
print "Los numeros escritos son:",num1,"y",num2
