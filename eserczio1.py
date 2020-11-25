candidato1 = input("Qual e il nome del primo candidato?")
candidato2 = input("Qual e il nome del secondo candidato?")
voti1 = int(input ("Quanti voti ha ottenuto " + candidato1 + "?"))
voti2 = int(input ("Quanti voti ha ottenuto " + candidato2 + "?"))
votitotali = voti1 + voti2
percentualevoti1= (voti1*100/votitotali)
percentualevoti2= (voti2*100/votitotali)
print (percentualevoti1 , "%" , candidato1)
print (percentualevoti2 , "%" , candidato2)
if percentualevoti1 > percentualevoti2:
    print("Complimenti, ha vinto " + candidato1)
else:
    print("Complimenti, ha vinto " + candidato2)