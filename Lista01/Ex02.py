# A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre
# o salário e número de filhos. Faça um procedimento que leia esses dados para um número não
# determinado de pessoas, calcule e exiba a média de salário da população (a condição de parada
# deve ser um flag com salário negativo). Faça um programa que acione o procedimento

def media() -> None:
    salario = 1
    salario_total = 0
    filhos_total = 0

    while salario >= 0:
        print("Digite o salario da familia: ")
        salario = float(input())
    
        print("Digite o numero de filhos da familia: ")
        filhos = float(input())

        salario_total += salario
        filhos_total += filhos

    media = salario_total / filhos_total
    print(media)

media()