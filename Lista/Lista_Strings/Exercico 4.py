# Um palíndromo é uma palavra ou frase que pode ser lida da mesma
# forma tanto da esquerda para a direita como da direita para a
# esquerda (desconsiderando os espaços em branco). Considere que a
# entrada não possui sinais de pontuação ou acentos. Escreva um
# programa que, dada uma string, verifique se ela é um palíndromo

palavra = input("Digite uma palavra: ").replace(" ", "").lower()
palindrome = palavra[::-1]

if palindrome == palavra:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

#Debug
print(palavra)
print(palindrome)

#Dica = texte com Socorram me subi no ônibus em Marrocos