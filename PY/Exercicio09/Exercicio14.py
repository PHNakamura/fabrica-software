print("Fazer um algoritmo para ler: número da conta do cliente, saldo, débito e crédito")
print("Calcular e escrever o saldo atual (saldo atual = saldo - débitpo + crédito)")
print("Testar se o saldo atual for maior ou igual a zero e escreve a mensagem: Saldo Positivo ou Saldo Negativo")
print(" \n")
conta = int(input("Digite o número da sua conta: "))
saldo = float(input("Digite o valor do seu saldo em conta: R$"))
debit = float(input("Digite o valor do débito gerado: R$"))
credit = float(input("Digite o valor do crédito gerado: R$"))
saldo_atual = saldo - debit + credit
print(" \n")
if saldo_atual>0:
    print("A conta", conta, "possuiu um saldo de R$", saldo_atual, "portanto ela está com SALDO POSITIVO")
else:
    print("A conta", conta, "está com o saldo de R$", saldo_atual, "portanto ela está com SALDO NEGATIVO")
