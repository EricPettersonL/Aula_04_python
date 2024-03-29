# Aula_04_pythonAula 04 | Type hint, Tipos complexos (Dicionários vs DataFrames Vs Tabelas Vs Excel) e Funções

Continuando os estudos em python.
Type hinting é uma funcionalidade do Python que permite especificar os tipos de dados de variáveis, parâmetros e valores de retorno no seu código. Isso ajuda a melhorar a legibilidade e a manutenção do código.

Tipos complexos como dicionários, DataFrames (comumente usados em bibliotecas como o pandas para manipulação de dados), tabelas e arquivos do Excel são usados para armazenar e manipular dados em formatos estruturados dentro de programas em Python.

Funções na programação são blocos de código projetados para realizar uma tarefa específica. Elas podem receber dados de entrada, realizar operações nesses dados e retornar resultados. Funções ajudam na organização do código, tornando-o reutilizável e mais fácil de entender.

## Exercícios de Listas e Dicionários

 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
 
 ```
 lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_numeros:
    print(numero**2)
 
 ```
 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
 ```
 lista_programas = ["Python", "Java", "C++", "JavaScript"]

for programa in lista_programas:
    if programa == "C++":
        lista_programas.remove("C++")
        lista_programas.append("Ruby")
print(lista_programas)


 ```
 3 .Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
 ```
 livros  = {
    "titulo": "Aprendendo Python",
    "autor": "Lucas",
    "ano": 2022
}
lista_livros = []

for livro in livros.items():
    lista_livros.append(livro)
    print(livro)

 ```
 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
 ```
 frase = "O rato roeu a roupa do rei de roma e o rei de roma roeu a roupa do rato"

dicionario = {}

for caractere in frase.lower():
    if caractere in dicionario:
        dicionario[caractere] += 1
    else:
        dicionario[caractere] = 1
print(dicionario)

 ```
 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
```
lista_frutas = ["maca", "banana", "cereja"]
dicionario_frutas = {"maca": 0.45, "banana": 0.30, "cereja": 0.65}

preco_total = 0

for fruta in lista_frutas:
    preco_total += dicionario_frutas[fruta]
print(f"O preco total da compra é de {preco_total:.2f} reais")

```
## Exercícios intermediários e mais avançados

 6. Eliminação de Duplicatas
 Objetivo: Dada uma lista de emails, remover todos os duplicados.
```

lista_email = ["a@a.com", "b@b.com", "a@a.com", "b@b.com", "c@c.com", "d@d.com"]
nova_lista_email = []
for email in lista_email:
    if email not in nova_lista_email:
        nova_lista_email.append(email)
print(nova_lista_email)

email_unico = list(set(lista_email))
print(email_unico)

```


 7. Filtragem de Dados
 Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
```
lista_idades = [18, 20, 25, 30, 35, 40, 10, 15, 12, 17, 16]
idades_maiores_ou_igual_18 = []

for idade in lista_idades:
    if idade >= 18:
        idades_maiores_ou_igual_18.append(idade)    
print(idades_maiores_ou_igual_18)

idades_validas = [idade for idade in lista_idades if idade >= 18]
print(idades_validas)

```

 8. Ordenação Personalizada
 Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
```
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

```


 9. Agregação de Dados
 Objetivo: Dado um conjunto de números, calcular a média.
```

conjunto_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
media = sum(conjunto_numeros) / len(conjunto_numeros)
print(f"A media dos valores {conjunto_numeros} é {media:.2f}")

```


 10. Divisão de Dados em Grupos
 Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
 ```
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

 ```

## Exercícios com Dicionários

 11. Atualização de Dados
 Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
```
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

```


 12. Fusão de Dicionários
 Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
```
dicionario_1 = {"a": 1, "b": 2}
dicionario_2 = {"c": 3, "d": 4}

dicionario_3 = {**dicionario_1, **dicionario_2}
print(dicionario_3)

dicionario_1.update(dicionario_2)
print(dicionario_1)


```


 13. Filtragem de Dados em Dicionário
 Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
```

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

```


 14. Extração de Chaves e Valores
 Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
```
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


```


 15. Contagem de Frequência de Itens
 Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
```

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
```


## Exercícios de Funções

 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
```
def soma_numeros(numeros):
    return sum(numeros)

soma = soma_numeros([1, 2, 3, 4, 5])
print(soma)


```


 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
```
def primo(numero):
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

print(primo(7))

```


 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
```
def reverso(string):
    return string[::-1]

print(reverso("Lucas"))

```


 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
```
def pares_numeros(numeros, numero):
    pares = []
    
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] + numeros[j] == numero:
                pares.append((numeros[i], numeros[j]))
    return pares

numeros = [1, 2, 3, 4, 5]
numero = 6

resultado = pares_numeros(numeros, numero)

print(f"As combinações que somam {numero} são:")
for par in resultado:
    print(par)


```


 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.
```
def chaves_ordenadas(dicionario):
    return sorted(dicionario.keys())

dicionario = {'d': 1, 'b': 2, 'a': 3, 'e': 4, 'c': 5}
chaves = chaves_ordenadas(dicionario)

print(chaves)

```

## Desafio 

Usando o mesmo desafio passado, agora colocando funções nas formulas
```
bonus_2024: int = 1000

# Solicite ao usuario que digite seu nome
# Verificar se o nome foi preenchido
# Verificar se o nome não contém apenas espacos em branco	
# Verificar se o nome não contem números
# Ficar retornando para o programa caso o nome seja inválido

def verificar_nome(nome: str):
    while True:
        
        if nome == "":
            print("O nome deve ser preenchido")
            nome = input("Digite seu nome: ")
        elif nome.isspace():
            print("O nome não deve conter apenas espaços em branco")
            nome = input("Digite seu nome: ")
        elif any(char.isdigit() for char in nome):
            print("Seu nome deve conter apenas letras")
            nome = input("Digite seu nome: ")
        else:
            break
    return nome


# Solicite ao usuario que digite o valor do seu salário
# Verificar se o valor do salário foi preenchido
# Verificar se o valor do salário é um número
# Verificar se o valor do salário é maior que zero

def verificar_salario(salario: float):
    while True:
        
        try:
        
            if salario == "":
                print("O valor do salario deve ser preenchido")
                salario = input("Digite seu salario: ")
            elif salario.isspace():
                print("O valor do salario deve ser preenchido")
                salario = input("Digite seu salario: ")
            elif not any(char.isdigit() for char in salario):
                print("O valor do salario deve ser um numero")
                salario = input("Digite seu salario: ")
            elif any(test == "," for test in salario):
                print("O valor deve usar ponto em vez de virgula")
                salario = input("Digite seu salario: ")
            else:
                salario = float(salario)
                if float(salario) <= 0:
                    print("O valor do salario deve ser maior que zero")
                    salario = input("Digite seu salario: ")
                else:
                    break
        except ValueError as e:
            print(e)
    return salario
        
   
# Solicite ao usuario que digite o valor do bônus recebido
# Verificar se o valor do salário foi preenchido
# Verificar se o valor do salário é um número
# Verificar se o valor do salário é maior que zero

def verificar_bonus(bonus: float):
    while True:
        
        try:
            if bonus == "":
                print("O valor do bonus deve ser preenchido")
                bonus = input("Digite seu bonus: ")
            elif not any(char.isdigit() for char in bonus):    
                print("O valor do bonus deve ser um número")
                bonus = input("Digite seu bonus: ")
            elif any(test == "," for test in bonus):
                print("O valor deve usar ponto em vez de virgula")
                bonus = input("Digite seu bonus: ")
            else:
                bonus = float(bonus)
                if float(bonus) <= 0:
                    print("O valor do bonus deve ser maior que zero")
                    bonus = input("Digite seu bonus: ")
                else:
                    break    
        except ValueError as e:
            print(e)
    return bonus

# Calcule o valor do bônus final
nome = verificar_nome(input("Digite seu nome: "))
salario = verificar_salario(input("Digite seu salario: "))
bonus = verificar_bonus(input("Digite seu bonus: "))


final_bonus = (salario*bonus)

# Imprima o cálculo do KPI para o usuário
# Imprima a mensagem personalizada incluindo o nome do usuário, e o valor do bônus

kpi_2 = (bonus_2024 + final_bonus)
print(f"Oi {nome} seu bônus final ficou em {kpi_2:.2f} reais")

```

