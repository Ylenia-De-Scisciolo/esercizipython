totalestipendi = 0
numerostipendi = 0
while True:
    stipendio = input("Inserire uno stipendio")
    if stipendio == -1:
        break
    else:
        stipendio = int(stipendio)
        totalestipendi += stipendio
        numerostipendi += 1
media = int(totalestipendi/numerostipendi)
print("La media degli stipendi e dunque ", media)