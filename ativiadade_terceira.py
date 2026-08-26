#receba três valores e diga qual deles é maior
num1 = int(input("Digite numero1: "))
num2 = int(input("Digite numero2: ")) 
num3 = int(input("Digite numero3: "))

if num1 > num2 and num1 > num3:
 print( num1,"é o maior numero")
elif num2 > num1 and num2 > num3:
 print( num2,"é o maior numero")
else: 
 print( num3,"é o maior numero")