# Exercícios intermediários e mais avançados

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
lista_email = ["a@a.com", "b@b.com", "a@a.com", "b@b.com", "c@c.com", "d@d.com"]
nova_lista_email = []
for email in lista_email:
    if email not in nova_lista_email:
        nova_lista_email.append(email)
print(nova_lista_email)

email_unico = list(set(lista_email))
print(email_unico)

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

lista_idades = [18, 20, 25, 30, 35, 40, 10, 15, 12, 17, 16]
idades_maiores_ou_igual_18 = []

for idade in lista_idades:
    if idade >= 18:
        idades_maiores_ou_igual_18.append(idade)    
print(idades_maiores_ou_igual_18)

idades_validas = [idade for idade in lista_idades if idade >= 18]
print(idades_validas)

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
lista_pessoas = [
    {"nome": "João", "idade": 30},
    {"nome": "Maria", "idade": 25},
    {"nome": "Pedro", "idade": 20},
    {"nome": "Ana", "idade": 35},
    {"nome": "Lucas", "idade": 40}
]
lista_ordenada = sorted(lista_pessoas, key=lambda pessoa: pessoa["nome"])

print(lista_ordenada)

lista_pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(lista_pessoas)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
conjunto_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
media = sum(conjunto_numeros) / len(conjunto_numeros)
print(f"A media dos valores {conjunto_numeros} é {media:.2f}")


# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
lista_valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
impares = []

for valor in lista_valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f"Pares: {pares}")
print(f"Impares: {impares}")

pares_2 = [valor for valor in lista_valores if valor % 2 == 0]
impares_2 = [valor for valor in lista_valores if valor % 2 != 0]

print(f"Pares: {pares_2}")
print(f"Impares: {impares_2}")

