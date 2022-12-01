print:("Fazer um programa que verifique se uma letra digitada é F ou M")
print:("Conforme a letra escrever: F- Feminino, M - Masculino, Sexo Inválido")
print("\n")
gender = input("Digite o gênero (F para FEMININO ou M para MASCULINO): ")
if gender == "F" or gender == "f":
    print("O gênero é FEMININO.")
elif gender == "M" or gender == "m":
    print("O gênero é MASCULINO.")
else:
    print("Gênero inválido")
