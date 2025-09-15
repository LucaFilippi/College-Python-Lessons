# Escreva um programa que, dada uma string representando um texto,
# imprima o número de palavras existentes. Observação: você deve
# remover os sinais de pontuação (“.”, “,”, “:”, “;”, “!” e “?”)
# antes de realizar a contagem das palavras

import string

texto = input("Digite um texto: ")
texto_limpo = texto.translate(str.maketrans('', '', string.punctuation))
palavras = texto_limpo.split()
num_palavras = len(palavras)
print(f"O número de palavras no texto é: {num_palavras}")

#Debug
print(palavras)