valorTotalCompras= float(input("qual é o valor total das compras? R$ ?"))

if valorTotalCompras<=100:
    print(f"o valor total sem desconto {valorTotalCompras:.2f}")
    
elif valorTotalCompras <=300:
    desconto = valorTotalCompras * 5/100
    valorComDesconto = valorTotalCompras - desconto
    print(f"a sua compra foi de R$ {valorTotalCompras:.2f} Reais e o desconto de 5% foi de R$ {desconto:.2f} Reais a compra final com o desconto foi de R$ {valorComDesconto:.2f} Reais")

elif valorTotalCompras <=500:
    desconto = valorTotalCompras * 10/100
    valorComDesconto = valorTotalCompras - desconto
    print(f"a sua compra foi de R$ {valorTotalCompras:.2f} Reais e o desconto de 10% foi de R$ {desconto:.2f} Reais a compra final com o desconto foi de R$ {valorComDesconto:.2f} Reais")

else:
    desconto = valorTotalCompras * 15/100
    valorComDesconto = valorTotalCompras - desconto
    print(f"a sua compra foi de R$ {valorTotalCompras:.2f} Reais e o desconto de 15% foi de R$ {desconto:.2f} Reais a compra final com o desconto foi de R$ {valorComDesconto:.2f} Reais")


