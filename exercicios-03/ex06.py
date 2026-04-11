def calc(num1, num2, operacao):
    match operacao:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Erro: Divisão por zero"
        case _:
            return "Operação inválida"
