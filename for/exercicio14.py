
# Exercício 14: Análise de Desempenho de Vendas
# Enunciado: Uma empresa monitora as vendas mensais de seus analistas através de uma lista de valores float:
# vendas = [1200.50, 3400.00, 980.00, 5600.20, 2100.00, 850.00].
# Crie um script que percorra essa lista e gere uma nova lista contendo apenas as vendas que foram acima da média de faturamento da equipe.


vendas = [1200.50, 3400.00, 980.00, 5600.20, 2100.00, 850.00]



media_faturamento = sum(vendas) / len(vendas)

vendas_acima_da_media = []

for venda in vendas:
    if venda > media_faturamento:
        vendas_acima_da_media.append(venda)

print(f"Média de faturamento da equipe: R$ {media_faturamento:.2f}")
print(f"Vendas acima da média: {vendas_acima_da_media}")