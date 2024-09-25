# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de
# S, calculado segundo a fórmula abaixo.

def calcula(n: int) -> float:
   fatorial = n
   teste = n
   
   for i in range(teste - 1):
      n -= 1
      fatorial *= n 
    

print("Digite um valor inteiro e positivo N: ")
n = int(input())

print(calcula(n))