numPar = 0
numImpar = 0

numeros = []

print("Digite 10 números:")
while len(numeros) < 10:
    numero = int(input())
    numeros.append(numero)
    if numero % 2 == 0:
        numPar += 1
    else:
        numImpar += 1

print("A quantidade de números pares é:", numPar)
print("A quantidade de números ímpares é:", numImpar)
