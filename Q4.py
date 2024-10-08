popA = 80000
popB = 200000

cresA = 0.03
cresB = 0.015

anos = 0

while popA < popB:
    popA += popA * cresA
    popB += popB * cresB
    anos += 1

print("Se passarão:",anos, "anos até esse dia!")
