listacandidati = []
candidato1 = input("Qual e il nome del primo candidato?")
candidato2 = input("Qual e il nome del secondo candidato?")
lista.append(candidato1)
lista.append(candidato2)
lista.sort()
print(lista)
voti1 = int(input("Quanti voti ha ottenuto "+ candidato1 + "?"))
voti2 = int(input("quanti voti ha ottenuto "+ candidato2 + "?"))
voti = []
voti.append(voti1)
voti.append(voti2)
if voti1 > voti2:
    print("Complimenti, ha vinto " + candidato1)
else:
    print("Complimenti, ha vinto " + cand2)
voti.reverse ()
print(voti)