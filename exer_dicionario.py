# Exercícios com Dicionários
# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

lista_produtos = [
    { "nome": "arroz", "preco": 5.00},
    { "nome": "feijao", "preco": 3.00},
    { "nome": "macarrao", "preco": 2.00},
    { "nome": "molho", "preco": 1.00}
]
lista_atualizada = []

for item in lista_produtos:
    if item["nome"] == "feijao":
        item["preco"] = 4.00
    lista_atualizada.append(item)
print(lista_atualizada)

for item in lista_produtos:
    if item["nome"] == "arroz":
        item.update({"preco": 6.00})
print(lista_produtos)

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
dicionario_1 = {"a": 1, "b": 2}
dicionario_2 = {"c": 3, "d": 4}

dicionario_3 = {**dicionario_1, **dicionario_2}
print(dicionario_3)

dicionario_1.update(dicionario_2)
print(dicionario_1)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque_produtos = {
    "arroz": 10,
    "feijao": 0,
    "macarrao": 3,
    "molho": 0
}
for item in estoque_produtos.items():
    if item[1] > 0:
        print(item)

estoque_positivo = {item[0]: item[1] for item in estoque_produtos.items() if item[1] > 0}
print(estoque_positivo)


# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
pessoas = {
    "nome": "Lucas",
    "idade": 20,
    "profissão": "Programador"
}
dados_chaves = []
dados_valores = []

for item in pessoas.items():
    dados_chaves.append(item[0])
    dados_valores.append(item[1])
print(dados_chaves)
print(dados_valores) 

chaves = list(pessoas.keys())
valores = list(pessoas.values())
print(chaves)
print(valores)   


# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

frase = "Um prazo legal de programação em Python"

frequencia = {}

for caractere in frase.lower():
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1
print(frequencia)

# Agora contar as palavras se repetem em uma string

frase_2 = "O rato roeu a roupa do rei de roma e o rei de roma roeu a roupa do Rato de Roma"

frequencia_2 = {}

for palavra in frase_2.lower().split():
    if palavra in frequencia_2:
        frequencia_2[palavra] += 1
    else:
        frequencia_2[palavra] = 1
print(frequencia_2)