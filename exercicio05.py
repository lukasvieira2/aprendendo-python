from xml.dom.minidom import ProcessingInstruction

nu1 = float(input("digite um numero!  "))
nu2 = float(input("digite um numero!  "))

if nu1 > nu2:
    print(f"o numero {nu1} e maior! ")
else:
    print(f"o numero{nu2} e menor!")