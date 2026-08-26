#faça um programa que só valide a entrada do usuario se ele digitar um numero maior que 0
numero = int(input("Digite um número: "))

while numero <= 0:
    print(" numero invalido ")
    numero = int(input(" Digite novamente "))
print(" você digitou um numero positivo ")    
