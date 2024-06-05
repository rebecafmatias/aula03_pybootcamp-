nome_completo = input('Digite seu nome completo: ')
nome = nome_completo.split()
idade = None
salario = None


while len(nome) <= 1:
    nome_completo = input('Você digitou um valor inválido. \nInforme seu nome completo (nome + sobrenome): ')
    nome = nome_completo.split()

while idade == None:
    try:
        idade = int(input('Digite sua idade: ').strip())
    except ValueError:
        print('Você digitou um valor inválido, tente novamente. \nExemplo idade: 25')
        idade = None

while salario == None:
    try:
        salario = float(input('Digite seu salário: ').strip())
    except ValueError:
        print('Você digitou um valor inválido, tente novamente. \nExemplo salário: 1580.50')
        salario = None

