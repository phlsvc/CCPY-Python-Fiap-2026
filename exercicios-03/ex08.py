salario=int(input("Digite o salário: "))
aumento=0
if salario<=280:
    aumento=salario*0.20
elif salario>280 and salario<=700:
    aumento=salario*0.15
elif salario>700 and salario<=1500:
    aumento=salario*0.10
else:
    aumento=salario*0.05
print(f"O salário antes do aumento era: {salario}")
print(f"O percentual de aumento aplicado é: {aumento/salario*100}%")
print(f"O valor do aumento é: {aumento}")
print(f"O novo salário, após o aumento, é: {salario+aumento}")