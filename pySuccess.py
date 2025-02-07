linhas = int(input("Qual é o número de linhas desejado?: "))
piramide = []

for n in range(linhas):
    piramide.append([])
    piramide[n].append(1)
    for m in range(1,n):
        piramide[n].append(piramide[n - 1][m - 1] + piramide[n - 1][m])
    if n > 0 :
        piramide[n].append(1)
    print(piramide[n])