salaInicio = 1000
anoInicio = 1995
anoFinal = 2025
aumento = 0.015
salario = salaInicio * aumento 

for ano in range(anoInicio,anoFinal): 
    aumento *= 2
    salario *= aumento

print("Salário em", anoFinal, "é de:", salario)