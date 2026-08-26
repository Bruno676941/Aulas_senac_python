matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz)
print(matriz[2][0])
#primeiro ele vai pegar a lista, pois é a primeira coisa que ele identifica na variavel
for linha in matriz:
    # depois que ele identifica a lista a gente vai pedir para ele identificar o valor dentro da lista
    for valor in linha:
        print(valor)
        #só dá para usar em listas/matrizes