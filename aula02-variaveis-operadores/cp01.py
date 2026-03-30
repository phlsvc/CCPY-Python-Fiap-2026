nome= input("Digite o nome do colaborador: ")
valor= float(input("Digite o valor de hora trabalhada: "))
quantidade= float(input("Digite a quantidade de horas trabalhadas: "))
bonus= float(input("Digite o valor do bônus: "))
desconto= float(input("Digite o valor do desconto: "))
bruto= (valor * quantidade) + bonus
liquido= bruto - desconto
print("Colaborador: ", nome)
print("Salário Bruto: R$", bruto)
print("Salário Líquido: R$", liquido)