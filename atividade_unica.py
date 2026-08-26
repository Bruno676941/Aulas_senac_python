#primeira questão - faça um programa onde duas notas são pedidas
#depois calcule a medias delas e coloque:
# se a media for maior que 7 = "aprovado"
# se for menor ou igual a 6 = "aprovado"

nota1 = float(input("digite a primeira nota "))
nota2 = float(input("digite a segunda nota "))
media = (nota1 + nota2)/2
if media >= 7:
    print("aprovado")
else: 
 print("reprovado")