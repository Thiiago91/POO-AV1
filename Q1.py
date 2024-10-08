numeroTab = int(input("Informe um numero de 1 à 10: "))
if numeroTab >= 1 and numeroTab <= 10:
    tabuada = 1
    print("Tabuada do", numeroTab, ":")
    while tabuada <= 10:
        resultado = numeroTab * tabuada
        tabuada += 1
        print (numeroTab, "x", tabuada, "=", resultado)
