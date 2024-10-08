gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']


respostas = []
resultado = []
acertos = 0

respostas.append(input("Qual a resposta da questão? "))
respostas.append(input("Qual a resposta da questão? "))
respostas.append(input("Qual a resposta da questão? "))
respostas.append(input("Qual a resposta da questão? "))
respostas.append(input("Qual a resposta da questão? "))
respostas.append(input("Qual a resposta da questão? "))
respostas.append(input("Qual a resposta da questão? "))
respostas.append(input("Qual a resposta da questão? "))
respostas.append(input("Qual a resposta da questão? "))
respostas.append(input("Qual a resposta da questão? "))

for prova in range(10):
    if respostas[prova] == gabarito[prova]:
        resultado.append("Correto")
        acertos +=1
    else:
        resultado.append("Errado")
        
for prova in range(10):
    print(f"Questão {prova + 1} : {respostas[prova]} - {resultado[prova]}")
print("Quantidade de acertos:",acertos)
    