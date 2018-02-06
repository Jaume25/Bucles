#Coding: UTF8

x=int(input("Escriba un numero par: "))

while x%2 != 0:
	x=int(input("Escriba un numero par: "))
resp=raw_input("Quiere escribir otro numero par? (S/N) ")
while resp == "S" or resp == "s":
	x=int(input("Escriba otro numero par: "))
	while x%2 != 0:
		x=int(input("Escriba otro numero par: "))
	resp=raw_input("Quiere escribir otro numero par? (S/N) ")

	
				
		


