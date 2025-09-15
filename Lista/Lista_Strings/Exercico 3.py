# Escreva um programa que, dada uma string texto e uma string
# palavra, ache todas as posições de ocorrência da palavra no
# texto. O seu programa deve desconsiderar se as letras são
# maiúsculas ou minúsculas

text = input("Digite um texto: ").lower()
word  = input("Digite uma palavra: ").lower()

positions = []
index = text.find(word)
while index != -1:
    positions.append(index)
    index = text.find(word, index + 1)
print(f"A palavra '{word}' ocorre nas posições: {positions}")
positions_lenght = len(positions)
print(f"A palavra '{word}' ocorre {positions_lenght} vezes no texto.")
#Debug
print(positions)
print(positions_lenght)
