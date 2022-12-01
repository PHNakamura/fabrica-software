print("fazer um programa que leia três números e mostre o maior e o menor deles.")
print(" \n")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número:  "))
n3 = float(input("Digite o terceiro número: "))
print(" \n")
if n1 > n2 and n1 > n3:
    print("O número", n1, "é maior que o número", n2, "e também é maior que o", n3)
elif n1 == n2 and n1 == n3:
    print("Todos os números são iguais.")
elif n1 < n2 and n1 < n3:
    print("O número", n1, "é menor que o número", n2, "e também é menor que o número", n3)
elif n2 < n3 and n2 < n1:
    print(f"O número {n2} é menor que o número {n3} e também é menor que o número {n1}")
else:
    print(f"O número {n3} é menor que o número {n2} e também é menor que o número {n1}")
