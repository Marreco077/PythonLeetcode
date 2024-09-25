# Faça um procedimento que recebe a média final de um aluno, identifica e exibe o seu conceito,
# conforme a tabela abaixo. Faça um programa que leia a média de N alunos, acionando o proce-
# dimento para cada um deles. (N deve ser lido do teclado)

def media(media_aluno: int) -> None:
    conceito = ''
    if media_aluno >= 90:
        conceito = 'A'
    elif media_aluno >= 80:
        conceito = 'B'
    elif media_aluno >= 70:
        conceito = 'C'
    elif media_aluno >= 60:
        conceito = 'D'
    elif media_aluno >= 40:
        conceito = 'E'
    else:
        conceito = 'F'
    print(conceito)

print("Digite a quantidade de alunos: ")
alunos = int(input())

for i in range(alunos):
    print("Digite a media: ");
    media_aluno = int(input())

    media(media_aluno)