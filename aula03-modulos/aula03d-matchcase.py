escolha_usuario=input("escolhe fdp")
match escolha_usuario:
    case "0":
        print("sair do programa")
    case "1":
        print("entrar no programa")
    case _:
        print("erro")