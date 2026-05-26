
# Exercício 6: Buscador de E-mails Institucionais (Intermediário)
# Enunciado: Imagine que você tem uma lista de e-mails misturados: emails = ["joao@gmail.com", "maria@senac.df", "pedro@outlook.com", "ana@senac.df"]. Utilizando o for, percorra a lista e exiba no terminal apenas os e-mails que pertencem ao domínio institucional do Senac (@senac.df).

emails = ["joao@gmail.com", "maria@senac.df", "pedro@outlook.com", "ana@senac.df"]

for email in emails:

    if "gmail.com" in email:
        print(email)

