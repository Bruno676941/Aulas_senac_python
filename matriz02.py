#tutorial: matrizes contam os indices como listas e depois contam os indices de listas
#indices começam em 0 e depois são contados os elementos desse indice
matriz = [
    [40,60,80],
    [50,70,90],
    [10,20,30]
]
for etapa in range(len(matriz)):
 for etapa2 in range(len(matriz[etapa])):
  print("linha",etapa,"coluna",etapa2, " vale", matriz[etapa][etapa2])
     
   