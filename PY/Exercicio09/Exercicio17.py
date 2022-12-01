print("As organizações Tabajaram resolveram dar um aumento de salário aos seus colaboradores.")
print("Lhes contrataram para desenvolver o programa que calculará os reajustes.")
print("Fazer um rpograma que recebe o salário de um colaborador e o rajusta segundo o seguinte critério:")
print("Salário de até R$280,00 (incluindo): aumento de 20%")
print("Salário entre R$280,00 e R$700,00: aumento de 15%")
print("Salário entre 700,00 e R$1500,00: aumento de 10%")
print("Salários acima de R$1500,00: aumento de 5%")
print("Após o aumento ser realizado, informar na tela:")
print("O salário antes do reajuste: ")
print("O percentual de aumento aplicado: ")
print("O valor aumentado: ")
print("O novo salário, após o aumento")
print("\n")

au1 = 0.20
au2 = 0.15
au3 = 0.10
au4 = 0.05
sal = float(input("Digite o valor do salário (antes do aumento): "))
v_au1 = (sal * au1)
nv_sal1 = (sal * au1) + sal
v_au2 = (sal * au2)
nv_sal2 = (sal * au2) + sal
v_au3 = (sal*au3)
nv_sal3 = (sal*au3) + sal
v_au4 = (sal*au4)
nv_sal4 = (sal*au4) + sal
if sal <= 280.00:
    print(f"O aumento do salário foi de {sal*au1}. O percentual de aumento foi de {au1*100}%. Seu novo salário será de: R$ {nv_sal1}")
    print("Salário antes do reajuste: R$",sal)
    print("Percentual de aumento aplicado", au1*100,"%")
    print("Valor do aumento: R$",v_au1)
    print("Novo salário, após o aumento: ",nv_sal1)
elif sal > 280.00 and sal <= 700.00:
    print(f"O aumento do salário foi de R${sal*au2}. O percentual de aumento foi de {au2*100}%. Seu novo salário será de: R$ {nv_sal2}")
    print("Salário antes do reajuste: R$", sal)
    print("Percentual de aumento aplicado", au2*100,"%")
    print("Valor do aumento: R$", v_au2)
    print("Novo salário, após o aumento: ", nv_sal2)
elif sal > 700.00 and sal <= 1500.00:
    print(f"O aumento do salário foi de R${(sal*au3)}. O percentual de aumento foi de {au3*100}%. Seu novo salário será de: R$ {nv_sal3}")
    print("Salário antes do reajuste: R$", sal)
    print("Percentual do aumento aplicado: ", au3*100,"%")
    print("Valor do aumento: R$", v_au3)
    print("Novo salário, após o aumento: ", nv_sal3)
else:
#elif sal >=1500.00:
    print(f"O aumento do salário foi de R${(sal*au4)}. O percentual de aumento foi de {au4*100}%. Seu novo salário será de: R$ {nv_sal4}")
    print("Salário antes do reajuste: R$", sal)
    print("Percentual do aumento aplicado: ", au4*100,"%")
    print("Valor do aumento: R$",v_au4)
    print("Novo salário, após o aumento: ", nv_sal4)
