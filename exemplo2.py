#faça yum programinha que conte quantos numeros impares e numeros pares foram digitados
#durante um for o FOR é um conjunto maior que consome o if e else por exemplo:
pares = 0
impares = 0
for etapa in range(1,9):
  numero = int(input("Digite um número: "))
  if numero % 2 == 0:
    pares = pares + 1
  else:
    impares = impares + 1
print(" você tem ",impares," numeros impares")
print(" você tem ",pares," numeros pares")

