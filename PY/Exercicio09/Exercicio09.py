print("Fazer um algoritmo que leia o nome do aluno, o nome disiciplina, nota de 3 provas e calcular a media")
print("Verificar se o aluno foi aprovado, sabendo que a média deverá ser maior ou igual a 6,0")
print("Posteriormente imprimir o resultado de cada variavel linha a baixo de linha")
print(" \n")
aluno = input("Digite o nome do aluno: ")
disciplina01 = input("Digite o nome da disciplina 01: ")
disciplina02 = input("Digite o nome da disciplina 02: ")
disciplina03 = input("Digite o nome da disciplina 03: ")
nota01 = float(input("Digite a nota da disciplina 01: "))
nota02 = float(input("Digite a nota da disciplina 02: "))
nota03 = float(input("Digite a nota da disciplina 03: "))
media_notas = (nota01 + nota02 + nota03)/3
print(" \n")
print("Aluno: \n", aluno)
print(" \n")
print("Disciplina 01: \n",disciplina01)
print("Nota: "), nota01
print(" \n")
print("Disciplina 02:\n", disciplina02)
print("Nota: "), nota02
print(" \n")
print("Disciplina 03: \n", disciplina03)
print("Nota: "), nota03
print(" \n")
print("Média das três notas: ", media_notas)
print(" \n")
print("Resultado: ")
if media_notas >= 6:
    print("Aluno APROVADO")
else:
    print("Aluno REPROVADO")
