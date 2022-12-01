#print("Fazer um programa para cálculo de uma folha de pagamento.")
#print("Sabendo que os descontos são do IR, que depende do Sal. Bruto (conforme tabela abaixo)")
#print("3% Sindicato; 11% FGTS (Sal.Bruto - não descontado. A empresa quem deposita)")
#print("Salário líquido corresponde ao Sal. Bruto menos os descontos")
#print("O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês")
#print("Desconto do IR:")
#print("Sal. Bruto até 900 (inclusive) - isento")
#print("Sal. Bruto até 1500 (inclusive) - desconto de 5%")
#print("Sal. Bruto até 2500 (inclusive) - desconto de 10%")
#print("Sal. Bruto acima de 2500 - desconto de 20%")
#print("Imprima na tela as informações, dispostas conforme o exemplo abaixo.")
#print("No exemplo o valor da hora é 5 e a quantidade de hora é 220")
#print("Sal. Bruto (5*220):  R$ 1100,00")
#print("(-) IR (5%):         R$   55,00")
#print("(-) INSS(10%):       R$  110,00")
#print("FGTS (11%):          R$  121,00")
#print("Total de descontos:  R$  165,00")
#print("Salário Líquido:     R$  935,00")

# ACRESCENTAR O CÁLCULO da contribuição sindical (Com base no sal. bruto)
# Manter o desconto do INSS (sempre 10%)

val_hora = float(input("Digite o valor da sua hora trabalhada: R$ "))
qde_hora = float(input("Digite a quantidade de horas trabalhadas: "))
sal_bruto = val_hora*qde_hora

c_sind = 0.03
inss = 0.10
fgts = 0.11

vl_c_sind = sal_bruto * c_sind
v_inss = sal_bruto * inss
v_fgts = sal_bruto * fgts

p_ir1 = 0.00 #"Isento"
p_ir2 = 0.05
p_ir3 = 0.10
p_ir4 = 0.20

ir_desc1 = 0.00 #"Isento"
ir_desc2 = sal_bruto * p_ir2
ir_desc3 = sal_bruto * p_ir3
ir_desc4 = sal_bruto * p_ir4

vlt_900 = 900
vlt_1500 = 1500
vlt_2500 = 2500

ttl_desc1 = ir_desc1 + v_inss + sal_bruto*c_sind
ttl_desc2 = ir_desc2 + v_inss + sal_bruto*c_sind
ttl_desc3 = ir_desc3 + v_inss + sal_bruto*c_sind
ttl_desc4 = ir_desc4 + v_inss + sal_bruto*c_sind

print("\n")
print(f"Salário bruto (valor da hora trabalhada: R${val_hora:.2f} X quantidade de horas trabalhadas: {qde_hora})  total: R$ {sal_bruto:.2f}")
print("\n")
if sal_bruto <= vlt_900:
    print(f"O valor do salário bruto é de: R$ {sal_bruto:.2f} e é isento do IR.     O valor da Contr. Sindical({c_sind*100})% é de R${sal_bruto*c_sind:.2f}.     O valor do INSS({inss*100})% é de: R${v_inss:.2f}.     O valor do FGTS ({fgts*100})% é de: R${v_fgts:.2f}.     Total de descontos: R${ttl_desc1:.2f}.     Saldo líquido: R${sal_bruto-ttl_desc1:.2f}")
    print("\n")
    print("O valor do salário bruto é de: R$ {:.2f}.      O valor da Contribuição Sindical({})% é de {:.2f}     O valor do INSS({})% é de: R${:.2f}.     O valor do FGTS ({})% é de: R${:.2f}.     Total de descontos: R${:.2f}.     Saldo líquido: R${:.2f}".format(sal_bruto, c_sind*100, sal_bruto*c_sind, inss*100, v_inss, fgts*100, v_fgts, ttl_desc1,sal_bruto-ttl_desc1))
    print("\n")
    print("SALÁRIO BRUTO:......................R$", sal_bruto)
    print("(-) Contr.Sindical:.................R$", sal_bruto*c_sind)
    print("(-) IR (isento).....................R$", ir_desc1)
    print("(-) INSS (10%):.....................R$", v_inss)
    print("FGTS (11%) depositado em conta é :..R$", v_fgts)
    print("TOTAL DE DESCONTOS:.................R$", ttl_desc1)
    print("TOTAL À RECEBER (SALÁRIO LÍQUIDO)...R$", sal_bruto-ttl_desc1)
elif sal_bruto > 900 and sal_bruto <= 1500:
    print(f"O valor do salário bruto é de: R${sal_bruto:.2f} e o valor do IR({p_ir2})% é de {ir_desc2:.2f}.      O valor da Contr. Sindical({c_sind*100})% é de R${sal_bruto*c_sind:.2f}.      O valor do INSS({inss*100})% é de R${v_inss:.2f}.     Total de descontos: R${ttl_desc2:.2f}.     Salário líquido: R${sal_bruto-ttl_desc2:.2f}")
    print("\n")
    print("O valor do salário bruto é de {:.2f} e o valor do IR({:.2f})% é de {:.2f}.     O valor da Contr.Sindical({:.2f})% é de R${:.2f}.     O valor do INSS({:.2f})% é de R${:.2f}.     Total de descontos: R${:.2f}.     Salário líquido R${:.2f}".format(sal_bruto, p_ir2*100, ir_desc2, c_sind*100, sal_bruto*c_sind, inss*100, v_inss, ttl_desc2, sal_bruto-ttl_desc2))
    print("\n")
    print("SALÁRIO BRUTO:......................R$", sal_bruto)
    print("(-) Contr.Sindical (3%):............R$", sal_bruto * c_sind)
    print("(-) IR (5%).........................R$", ir_desc2)
    print("(-) INSS (10%):.....................R$", v_inss)
    print("FGTS (11%) DEPOSITADO EM CONTA É:...R$", v_fgts)
    print("TOTAL DE DESCONTOS:.................R$", ttl_desc2)
    print("TOTAL À RECEBER (SALÁRIO LÍQUIDO)...R$", sal_bruto - ttl_desc2)
elif sal_bruto > 1500 and sal_bruto <= 2500:
    print(f"O valor do salário bruto é de: R${sal_bruto:.2f} e o valor do IR({p_ir3*100})% é de {ir_desc3:.2f}.      O valor da Contr. Sindical({c_sind * 100})% é de R${sal_bruto * c_sind:.2f}.      O valor do INSS({inss * 100})% é de R${v_inss:.2f}.     Total de descontos: R${ttl_desc3:.2f}.     Salário líquido: R${sal_bruto - ttl_desc3:.2f}")
    print("\n")
    print("O valor do salário bruto é de {:.2f} e o valor do IR({:.2f})% é de {:.2f}.     O valor da Contr.Sindical({:.2f})% é de R${:.2f}.     O valor do INSS({:.2f})% é de R${:.2f}.     Total de descontos: R${:.2f}.     Salário líquido R${:.2f}".format(sal_bruto, p_ir3 * 100, ir_desc3, c_sind * 100, sal_bruto * c_sind, inss * 100, v_inss, ttl_desc3,sal_bruto - ttl_desc3))
    print("\n")
    print("SALÁRIO BRUTO:......................R$", sal_bruto)
    print("(-) Contr.Sindical (3%):............R$", sal_bruto * c_sind)
    print("(-) IR (10%)........................R$", ir_desc3)
    print("(-) INSS (10%):.....................R$", v_inss)
    print("FGTS (11%) DEPOSITADO EM CONTA É:...R$", v_fgts)
    print("TOTAL DE DESCONTOS:.................R$", ttl_desc3)
    print("TOTAL À RECEBER (SALÁRIO LÍQUIDO)...R$", sal_bruto - ttl_desc2)
elif sal_bruto >2500:
    print(f"O valor do salário burto é de: R${sal_bruto:.2f} e o valor do IR({p_ir4*100})% é de {ir_desc4:.2f}.     O valor da Contr.Sindical({c_sind*100})% é de R${sal_bruto*c_sind:.2f}.     O valor do INSS({inss*100})% é de R${v_inss:.2f}.     Total de descontos: R${ttl_desc4:.2f}.      Salário líquido: R${sal_bruto - ttl_desc4:.2f}")
    print("\n")
    print("O valor do salário bruto é de {:.2f} e o valor do IR({:.2f})% é de {:.2f}.     O valor da Contr.Sindical({:.2f})% é de R${:.2f}.     O valor do INSS({:.2f})% é de R${:.2f}.     Total de descontos: R${:.2f}.     Salário líquido R${:.2f}".format(sal_bruto, p_ir4 * 100, ir_desc4, c_sind * 100, sal_bruto * c_sind, inss * 100, v_inss, ttl_desc4, sal_bruto - ttl_desc4))
    print("\n")
    print("SALÁRIO BRUTO:......................R$", sal_bruto)
    print("(-) Contr.Sindical (3%):............R$", sal_bruto * c_sind)
    print("(-) IR (20%)........................R$", ir_desc4)
    print("(-) INSS (10%):.....................R$", v_inss)
    print("FGTS (11%) DEPOSITADO EM CONTA É:...R$", v_fgts)
    print("TOTAL DE DESCONTOS:.................R$", ttl_desc4)
    print("TOTAL À RECEBER (SALÁRIO LÍQUIDO)...R$", sal_bruto - ttl_desc2)
