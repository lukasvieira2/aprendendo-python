notas = [
    [7.0, 8.5, 6.0, 7.5],
    [9.0, 9.5, 10.0, 8.5],
    [5.0, 6.0, 5.5, 4.0]
]

medias = []


for linha in notas:
    soma_notas = sum(linha)
    quantidade_notas = len(linha)
    media_aluno = soma_notas / quantidade_notas
    medias.append(media_aluno)

for i, media in enumerate(medias):
    print(f"Média do Aluno {i + 1}: {media:.2f}")