# 1 Escreva um programa que, dada uma sequência de números inteiros
# (todos fornecidos na mesma linha, separados por espaços), imprima
# a média desses números

numeros = input("Digite uma sequência de números inteiros separados por espaços: ")
try: 
    lista_numeros = [int(num) for num in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros.")
    exit()
media = sum(lista_numeros) / len(lista_numeros)
print(f"A média dos números é: {media}")
