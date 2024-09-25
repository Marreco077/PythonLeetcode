# Faça um procedimento que recebe as 3 notas de um aluno por parâmetro e uma letra. Se a letra
# for ‘A’, o procedimento calcula e escreve a média aritmética das notas do aluno, se for ‘P’, calcula
# e escreve a sua média ponderada (pesos: 5, 3 e 2). Faça um programa que leia 3 notas de N
# alunos e acione o procedimento para cada aluno. (N deve ser lido do teclado)

def calcula(nota1: int, nota2: int, nota3: int, opcao):
    if opcao == 'A':
        print((nota1 + nota2+ nota3) / 3)
    elif opcao == 'P':
        print(((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 10)


print("Digite a quantidade de alunos:")
numero_alunos = int(input())

for i in range(numero_alunos):
    print(f"Digite a primeira nota do aluno {i+1}:")
    nota1 = int(input())
    
    print(f"Digite a segunda nota do aluno {i+1}:")
    nota2 = int(input())

    print(f"Digite a terceira nota do aluno {i+1}")
    nota3 = int(input())

    print("Digite se é media aritmetica ou ponderada [A/P]: ")
    opcao = input()

    calcula(nota1, nota2, nota3, opcao)
