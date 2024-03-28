# Exercícios de Listas e Dicionários

# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_numeros:
    print(numero**2)
    
# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista_programas = ["Python", "Java", "C++", "JavaScript"]

for programa in lista_programas:
    if programa == "C++":
        lista_programas.remove("C++")
        lista_programas.append("Ruby")
print(lista_programas)

# 3 .Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livros  = {
    "titulo": "Aprendendo Python",
    "autor": "Lucas",
    "ano": 2022
}
lista_livros = []

for livro in livros.items():
    lista_livros.append(livro)
    print(livro)

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

frase = "O rato roeu a roupa do rei de roma e o rei de roma roeu a roupa do rato"

dicionario = {}

for caractere in frase.lower():
    if caractere in dicionario:
        dicionario[caractere] += 1
    else:
        dicionario[caractere] = 1
print(dicionario)

# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_frutas = ["maca", "banana", "cereja"]
dicionario_frutas = {"maca": 0.45, "banana": 0.30, "cereja": 0.65}

preco_total = 0

for fruta in lista_frutas:
    preco_total += dicionario_frutas[fruta]
print(f"O preco total da compra é de {preco_total:.2f} reais") # preco_total)


# Exercícios com Dicionários
# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

# Exercícios de Funções
# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.
