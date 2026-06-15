idade = int(input("Digite a sua idade?   "))

if idade <= 9:
    print(f"Categoria: Mirim {idade} anos")
elif idade <= 14:
    print(f"Categoria: Infantil {idade:} anos")
elif idade <= 19:
    print(f"Categoria: Junior {idade:} anos")
elif idade <= 25:
    print(f"Categoria: senior {idade:} anos")
else:
    print(f"Categoria: master {idade:} anos")