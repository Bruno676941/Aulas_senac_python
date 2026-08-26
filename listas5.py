# Faça um programa que tenha como variável "preco_produtos"
# onde vai guardar uma lista de valores diferentes.
# Onde tem que criar um código que separe QUANTOS valores
# tem acima de RS 20,00
# e por fim faça a soma de todos os valores da lista

preco_produtos = [5, 15, 1915, 56, 41, 1993]
soma = 0
produto_acima_de_20 = 0

for i in preco_produtos:
   soma = soma + i
   if i > 20:
    produto_acima_de_20 = produto_acima_de_20 + 1
print(produto_acima_de_20, "São valores acima de 20 reais")
print("A soma de todos os valores foi de: ",soma)