sistemaBackend = ""
while True:
    sistemaBackend = input("Digite o ADMIN|GERENTE|EDITOR|VISITANTE :  ")
    match sistemaBackend.lower():
        case "admin":
            print("Acesso total: Criar, Ler, Atualizar e Deletar")

        case "gerente":
            print("Acesso gerencial: Criar, Ler e Atualizar")

        case "editor":
            print("Acesso de conteúdo: Ler e Atualizar")

        case "visitante":
            print("Acesso restrito: Apenas Leitura")

        case 0:
            break

        case _:
            print("Perfil não reconhecido. Acesso bloqueado.")