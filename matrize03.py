matriz = [
    [47,60,81],
    [53,70,91],
    [10,20,31]
]
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            print(valor, " é par")
        else:
            print(valor, " é impar")