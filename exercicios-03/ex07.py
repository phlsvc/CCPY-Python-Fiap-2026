ano_nascimento=int(input("Digite o ano de nascimento: "))
idade=2026-ano_nascimento
if idade>=18 and idade<=70:
    print("Voto obrigatório nesse ano")
elif idade>=16 and idade<18 or idade>70:
    print("Voto opcional nesse ano")
else:    print("Voto proibido nesse ano")
