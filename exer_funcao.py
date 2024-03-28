# Exercícios de Funções
# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def soma_numeros(numeros):
    return sum(numeros)

soma = soma_numeros([1, 2, 3, 4, 5])
print(soma)

# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def primo(numero):
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

print(primo(6))

# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

def reverso(string):
    return string[::-1]

print(reverso("Lucas"))

# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

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

    
# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.

def chaves_ordenadas(dicionario):
    return sorted(dicionario.keys())

dicionario = {'d': 1, 'b': 2, 'a': 3, 'e': 4, 'c': 5}
chaves = chaves_ordenadas(dicionario)

print(chaves)