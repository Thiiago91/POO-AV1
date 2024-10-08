numero = int(input("Digite um número:"))

numPrimo = True

if numero > 1:
        inteiro = 2
        while inteiro < numero and numPrimo:
            if (numero % inteiro) == 0:
                numPrimo = False
            inteiro += 1
else:
    numPrimo = False
if numPrimo:
    print(numero, "é  primo")
else:
    print(numero, "não é  primo")
