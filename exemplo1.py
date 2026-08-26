#faça um programa que adapte para calcular a some de números digitados pelo usuario (usar input, dentro do loop)
soma = 0
for etapa in range(1,9):
    numero = int(input("Digite um número: "))
    soma = soma + numero
print("soma dos numeros é: ", soma)