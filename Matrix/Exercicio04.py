vendas = [
    [1200, 850, 900, 1500],
    [900, 1100, 1000, 1300],
    [1500, 1600, 1400, 1800],
    [700, 600, 800, 900]
]

# Total vendido por cada vendedor
print("Total vendido por cada vendedor:")
for i in range(len(vendas)):
    total_vendedor = sum(vendas[i])
    print(f"Vendedor {i+1}: R$ {total_vendedor}")

# Total vendido por dia
print("\nTotal vendido por dia:")
for dia in range(len(vendas[0])):
    total_dia = 0
    for vendedor in range(len(vendas)):
        total_dia += vendas[vendedor][dia]
    print(f"Dia {dia+1}: R$ {total_dia}")