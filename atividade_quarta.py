#faça um programa que peça a idade do usuario. se ele tem entre 0 e 12 anos = criança 
# se ele tem entre 0 e 12 anos = criança
# se ele tem entre 13 e 17 anos = adolescente
# se ele tem entre 18 e 25 anos = jovem adulto
# se ele tem entre 26 e 59 anos = adulto
# se ele tem entre +60 anos = idoso

idade = int(input("Digite sua idade "))

if idade >= 0 and  idade <=  12:
 print(" Você é uma criança")
elif idade >= 13 and idade <= 17:
 print(" Você é um adolescente")
elif idade >= 18 and idade <= 25:
 print(" Você é um jovem adulto")
elif idade >= 26 and idade <= 59:
 print(" Você é um adulto")
else:
 print(" Você é um idoso")  