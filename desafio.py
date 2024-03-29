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