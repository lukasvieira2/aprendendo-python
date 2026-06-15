
# Execício 5: Validador de Senhas e Tentativas (Intermediário)
#  Enunciado: Um sistema de segurança permite que o usuário tente digitar sua senha de acesso no máximo 3 vezes. Crie um loop for que execute 3 vezes pedindo a senha. Se o usuário digitar a senha correta (defina uma senha padrão no código), o programa deve exibir "Acesso Permitido" e interromper o laço imediatamente usando o break. Se as 3 tentativas falharem, exiba "Conta Bloqueada".

usuario = []
senhaCorreta = 123
contador = 0
for i in range(3):
    senha = int(input("Diga sua senha: "))


    if senhaCorreta == senha:
        print(f"Acesso Permitido")
        break
    else:
        print(f"Senha Incorreto")

        contador += 1
if contador == 3:
    print(f"Conta Bloqueada")