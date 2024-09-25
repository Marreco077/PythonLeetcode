# Faça um procedimento que recebe 3 valores inteiros por parâmetro e os exiba em ordem crescente.
# Faça um programa que leia N conjuntos de 3 valores e acione o procedimento para cada conjunto.
# (N deve ser lido do teclado)

def maior(valor1: int, valor2: int, valor3: int) -> None:
    maior = valor1
    menor = valor2
    medio = valor3
    
    if valor2 > maior:
        maior = valor2
    if valor3 > maior:
        maior = valor3

    if valor1 < menor:
        menor = valor1
    if valor2 < menor:
        menor = valor2
    if valor3 < menor:
        menor = valor3
    
    if (valor1 > menor and valor1 < maior):
        medio = valor1
    elif (valor2 > menor and valor2 < maior):
        medio = valor2
    else:
        medio = valor3  # Se não for menor nem maior, deve ser o médio
    
    print(menor, medio, maior)

def maior_teste(valor1: int, valor2: int, valor3: int) -> None:
    vetor = [valor1, valor2, valor3]

    maior = valor1
    menor = valor2
    medio = valor3

    for numbers in vetor:
        if numbers > maior:
            maior = numbers
        if numbers < menor:
            menor = numbers
    
    for number in vetor:
        if number != maior and number != menor:
            medio = number
            break

    print(menor, medio, maior)

print("Digite a quantidade de conjuntos: ")
conjuntos = int(input())

for i in range(conjuntos):
    print("Digite os 3 valores: ")
    valor1 = int(input())
    valor2 = int(input())
    valor3 = int(input())

    maior_teste(valor1, valor2, valor3)
