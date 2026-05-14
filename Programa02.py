n1 = float (input ("Escreva o primeiro número: ").replace("," , "."))
n2 = float (input ("Escreva o segundo número: ").replace("," , "."))
n3 = float (input ("Escreva o terceiro numero: ").replace("," , "."))

media = (n1+n2+n3)/3
if media >= 7:
    print ("O aluno foi aprovado: ")

elif media <= 5:
    print ("O aluno está de recuperaçäo: ")
elif media <= 6:
     print ("O aluno está reprovado: ")