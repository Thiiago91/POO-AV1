p = 1.99

for quant in range(1, 50):
    valor = quant * 1.99

quantitens = int(input("Quantos itens comprou: "))
vt = quantitens * 1.99
listitens = input("Quais itens comprou: ")

print("Lojas Quase Dois - Tabela de preços")
print("Você comrprou", listitens)
print("Valor total para", quantitens, "itens: R$", vt)
