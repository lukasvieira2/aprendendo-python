# Cadastro de funcionários
funcionarios = {
    101: {"Nome": "Lucas", "Cargo": "Analista de TI", "Salario": 4200.00},
    102: {"Nome": "Mariana", "Cargo": "Designer Gráfico", "Salario": 2800.00},
    103: {"Nome": "Roberto", "Cargo": "Gerente de Projetos", "Salario": 6500.00},
    104: {"Nome": "Juliana", "Cargo": "Assistente Administrativo", "Salario": 2200.00}
}

print("Funcionários com salário acima de R$ 3.000,00:")
print("-" * 45)


for id_func, dados in funcionarios.items():
    if dados["Salario"] > 3000.00:
        print(f"Nome: {dados['Nome']} | Cargo: {dados['Cargo']} | Salário: R$ {dados['Salario']:.2f}")