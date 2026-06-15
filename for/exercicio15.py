# Exercício 15: Removendo Duplicatas de um Banco de Dados
# Enunciado: Simulando a limpeza de dados de um sistema migrado,
# você recebeu uma lista com IDs de clientes que contém elementos duplicados devido a falhas no sistema anterior:
# ids_clientes = [101, 102, 103, 101, 104, 102, 105, 106, 103].
# Escreva um algoritmo que remova todos os elementos duplicados dessa lista, mantendo apenas uma ocorrência de cada ID, sem utilizar a função

ids_clientes = [101, 102, 103, 101, 104, 102, 105, 106, 103]


ids_unicos = []


for id_cliente in ids_clientes:

    if id_cliente not in ids_unicos:
        ids_unicos.append(id_cliente)


print("Lista original:", ids_clientes)
print("Lista limpa (sem duplicatas):", ids_unicos)