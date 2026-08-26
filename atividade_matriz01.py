#faça um programa que guarde 4 notas de 3 alunos onde:
#O codigo deve percorrer linha a linha,
#para cada aluno, calcule a soma das 4 notas e depois dê a media delas
#diga se o aluno foi aprovado(media >= 6) ou reprovado.
#por fim dese imprimir, a média tirada e se foi aprovado ou reprovaqdo

matriz = [
    [4,6,8,7],
    [5,7,8,0],
    [9,8,7,6],

]
for linha in matriz:
    soma = linha[0]+linha[1]+linha[2]+linha[3] 
    media = soma /4
    if media >= 6:
            print(media, " Aluno passado")
    else:
            print(media, " aluno reprovado")
   