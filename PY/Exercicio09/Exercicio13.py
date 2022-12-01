print("Fazer um algoritmo que leia o número digitado é par ou ímpar")
print(" \n")
num = int(input("Digite um número: "))
print(" \n")
if num == 0:
    print("O número", num, "é neutro")
elif num%2 == 0:
    print("O número digitado é PAR")
else:
    print("O número digitado é IMPAR")
