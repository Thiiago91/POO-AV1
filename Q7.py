valorDaDivida = int(input("Tá devendo quanto? "))

parcelas = [1,3,6,9,12]
juros = [0,10,15,20,25]

print("\nTabela de juros sobre a quantidade de parcealas")
print("Divida | Juros | Quantidade de ´Parcelas | Valor da Parcela")

for tabela in range(len(parcelas)):
    valorDosJuros = valorDaDivida * juros[tabela]
    valorTotal = valorDaDivida + valorDosJuros
    valorDaParcela = valorTotal / parcelas[tabela]
    print(parcelas[tabela], "|", juros[tabela]," | R$", valorDaParcela, "| R$", valorTotal)