numeros = [10, 20, 30, 40, 50]

print(numeros)

print(numeros[0]) # Começa do zero <-
print(numeros[4])
print(numeros[3])

print(len(numeros)) # len() Mostra quantos elementos tem na lista 

numeros.append(60) # .append Adiciona um elemento no final
print(numeros)

numeros[2] = "spinosaurus" # Altera o valor de um dos índices
print(numeros)

numeros.remove(50) # .remove Remove um elemento
print(numeros)