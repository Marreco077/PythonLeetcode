# Escreva um procedimento que recebe 3 valores reais X, Y e Z e que verifique se esses valores podem
# ser os comprimentos dos lados de um triângulo e, neste caso, exibe qual é o tipo de triângulo
# formado. Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja
# satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma do comprimento
# dos outros dois lados. O procedimento deve identificar o tipo de triângulo formado observando
# as seguintes definições:
# • Triângulo Equilátero: os comprimentos dos 3 lados são iguais;
# • Triângulo Isósceles: os comprimentos de pelo menos 2 lados são iguais.
# • Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.
# Faça um programa que leia um número indeterminado (até lado negativo) de triângulos (valores
# dos 3 lados) e para cada triângulo, acione o procedimento.

def triangulo(lado1: int, lado2: int, lado3: int):
    
    if lado1 == lado2 and lado1 == lado3:
        print("Triangulo equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triangulo isosceles")
    else:
        print("Triangulo Escaleno")

def eh_triangulo(lado1: int, lado2: int, lado3: int):
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        triangulo(lado1, lado2, lado3)
    else:
        print("Não é triangulo")

lado1 = 0

while lado1 >= 0:
    print("Digite os 3 lados de um triangulo: ")
    lado1 = int(input())
    lado2 = int(input())
    lado3 = int(input())
    if(lado1 >= 0):
        eh_triangulo(lado1, lado2, lado3)