print("Fazer um algoritmo que verifique se o número digitado é positivo ou negativo")
print(" \n")
num = int(input("Digite o número:"))
#print(" \n")
if num < 0:
    print("O número", num, "é NEGATIVO")
elif num > 0:
    print("O número", num, "é POSITIVO")
else:
    print("O número", num, "é considerado neutro")
