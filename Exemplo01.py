#1.(15 > 7) && (3==3)
#2.(10 < 4) || (8 != 5)
#3.!(20 >= 20)
#4.(5*2 == 10) && !(3 > 4)
#5.(12/2 == 5) || (7 <= 7)
#6.!(9 != 9) && (4 > 1)
#7.(100 == 100) && ((5! = 5)||(2 < 3))
#8.!((18 < 20)&&(5 != 5))
#9.(0 == 1) || !((3 >= 2) && (4 <= 4))
#10 ((10 > 5) && !(2 == 3)) || (8 < 4)

a1 = (15 > 7)
b1 = (3==3)
a2 = (10 < 4)
b2 =  (8 != 5)
a3 = (20 >= 20)
a4 = (5*2 == 10)
b4 =  (3 > 4)
a5 = (12/2 == 5)
b5 = (7 <= 7)
a6 = (9 != 9)
b6 = (4 > 1)
a7 = (100 == 100)
b7 = ((5 == 5) or (2 < 3))
a8 =  ((18 < 20) and (5 != 5))
a9 = (0 == 1)
b9 = ((3 >= 2) and (4 <= 4))
a10 = ((10 > 5) and not (2 == 3)) or (8 < 4)

ex1 = a1 and b1
ex2 = a2 or b2
ex3 = not a3
ex4 = (5*2 == 10) and not b4
ex5 = a5 or b5
ex6 = a6 and b6
ex7 = a7 and b7
ex8 = not a8
ex9 = a9 or not b9
ex10 = a10

print(f"exercicio 01 {ex1}")
print(f"exercicio 02 {ex2}")
print(f"exercicio 03 {ex3}")
print(f"exercicio 04 {ex4}")
print(f"exercicio 05 {ex5}")
print(f"exercicio 06 {ex6}")
print(f"exercicio 07 {ex7}")
print(f"exercicio 08 {ex8}")
print(f"exercicio 09 {ex9}")
print(f"exercicio 10 {ex10}")