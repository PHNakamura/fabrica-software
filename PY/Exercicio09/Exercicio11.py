print("Fazer um algoritmo que o usuário possa digitar o seu nome e a sua idade")
print("Utilizar a tablea e verificar onde se enquadra a idade da pessoa")
print("Escreva a mensagem: (nome) está com (idade) e pela tabela é considerado um (tipo)")
print(" \n")
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
#bebe = 0 a 2
#crianca = 3 a 11
#jovem = 12 a 21
#adulto = 22 a 64
#idoso = 65 a 100
# muito_velhinho > 101

if idade <= 2:
    print(nome, "está com", idade,"anos e pela tabela é considerado um bebe")
elif idade >= 3 and idade <= 11:
    print(nome, "está com", idade, "anos e pela tabela é considerado uma criança")
elif idade >= 12 and idade <= 21:
    print(nome, "está com", idade, "anos e pela tabela é considerado um jovem")
elif idade >= 22 and idade <= 64:
    print(nome, "está com", idade, "anos e pela tabela é considerado um adulto")
elif idade >= 65 and idade <=100:
    print(nome, "está com", idade, "anos e pela tabela é onsiderado um idoso")
else:
    print(nome, "está com", idade, "anos e pela tabela é considerado muito velhinho")
