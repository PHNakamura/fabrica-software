#print("Fazer um programa que peça os três lados de um triângulo.")
#print("Indique, caso osmlados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.")

s1 = float(input("Digite o primeiro segmento de reta: "))
s2 = float(input("Digite o segundo segmento de reta: "))
s3 = float(input("Digite o terceiro segmento de reta: "))
#A soma das medidas de dois deles  é sempre  que a medida do terceiro, então, elas podem formar um triângulo.
print("\n")
if s1 == s2 == s3:
    print("Os segmentos de reta formam um triângulo")
    print("\n")
    print("O triângulo formado será EQUILÁTERO")
elif s1==s2!=s3:
    print("Os segmentos de reta formam um triângulo")
    print("\n")
    print("O triângulo formado será Isósceles")
elif s1!=s2!=s3:
    print("Os segmentos de reta formam um triângulo")
    print("\n")
    print("O triângulo formado será escaleno")
