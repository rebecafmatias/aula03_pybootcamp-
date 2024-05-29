"""Exercício 1: Verificação de Qualidade de Dados
Você está analisando um conjunto de dados de vendas e precisa garantir 
que todos os registros tenham valores positivos para `quantidade` e `preço`. 
Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
forem positivos ou "Dados inválidos" caso contrário."""

quantidade = int(input("Quantidade: "))
preco = float(input("Preço: "))

if quantidade > 0 and preco > 0:
    print('Dados válidos')
else:
    print('Dados inválidos')

"""Exercício 2: Classificação de Dados de Sensor
Imagine que você está trabalhando com dados de sensores IoT. 
Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

    Temperatura < 18°C é 'Baixa'
    Temperatura >= 18°C e <= 26°C é 'Normal'
    Temperatura > 26°C é 'Alta'
"""

temp = float(input("Temperatura: "))

if temp < 18:
    temp_categoria = 'Baixa'
elif temp >= 18 and temp <= 26:
    temp_categoria = 'Normal'
elif temp > 26:
    temp_categoria = 'Alta'

print(temp_categoria)

"""Exercício 3: Filtragem de Logs por Severidade
Você está analisando logs de uma aplicação e precisa filtrar mensagens 
com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 
'Falha na conexão'}`, 
escreva um programa que imprima a mensagem se a severidade for 'ERROR'."""

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 
'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])


"""Exercício 4: Validação de Dados de Entrada
Antes de processar os dados de usuários em um sistema de recomendação, 
você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
fornecido um email válido. Escreva um programa que valide essas condições 
e imprima "Dados de usuário válidos" ou o erro específico encontrado."""

idade_user = 18
email_user = 'blablabla@gmail.com'

if idade_user >=18 and idade_user <= 65:
    if '@' in email_user:
        print("Dados de usuário válidos")
    else:
        print("Email inválido")
else:
    print("Idade fora do range permitido")

"""Exercício 5: Detecção de Anomalias em Dados de Transações
Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é 
suspeita."""

transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000:
    print('Transação suspeita')
elif transacao['hora'] < 9:
    print('Transação suspeita')
elif transacao['hora'] > 18:
    print('Transação suspeita')

"""Exercício 6. Contagem de Palavras em Textos
Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele."""

texto = 'Hoje é nossa terceira aula, é uma aula muito boa'
novo_texto = texto.replace(',','').lower()

palavras = novo_texto.split()

print(palavras)

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)

"""Exercício 7. Normalização de Dados
Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1."""

numeros = [10,15,30,45,11]
num_normalizados = []
print(numeros)

for i in numeros:
    num_normalizados.append((i - min(numeros)) / (max(numeros) - min(numeros)))
print(num_normalizados)


"""Exercício 8. Filtragem de Dados Faltantes
Objetivo:** Dada uma lista de dicionários representando dados de usuários, 
filtrar aqueles que têm um campo específico faltando"""

lista = [
    {'nome': 'Rebeca',
     'idade': 26,
     'email': 'rebeca@gmail.com',
     'profissao': 'Analista de dados'},
     {'nome': 'Isabella',
     'idade': 24,
     'email': '',
     'profissao': 'Assistente administrativo'},
     {'nome': 'Raquel',
     'idade': '',
     'email': 'raquel@gmail.com',
     'profissao': 'Militar'}
]

dados_faltantes = {}

for i in lista:
    if i['idade'] == '':
        print(f"Idade do usário {i['nome']} faltando")
        dados_faltantes.update({i['nome']:'idade'})
    elif i['email'] == '':
        print(f"Email do usário {i['nome']} faltando") 
        dados_faltantes.update({i['nome']:'email'})
    elif i['profissao'] == '':
        print(f"Profissão do usário {i['nome']} faltando") 
        dados_faltantes.update({i['nome']:'profissao'})

print(dados_faltantes)
    
"""Exercício 9. Extração de Subconjuntos de Dados
Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares."""

lista = [10,5,12,13,25,6,20]
lista_pares = []

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)

print(f'Numeros pares: {lista_pares}')

"""Exercício 10. Agregação de Dados por Categoria
Objetivo:** Dado um conjunto de registros de vendas, 
calcular o total de vendas por categoria."""

vendas = [
    {'key':'venda01','produto': 2000, 'servico': 150, 'consultoria':0},
    {'key':'venda02','produto': 1500, 'servico': 200, 'consultoria':0},
    {'key':'venda03','produto': 300, 'servico': 200, 'consultoria':1500}
]

vendas_consolidado = {}

for venda in vendas:
    for tipo_venda, valor in venda.items():
        if tipo_venda != 'key':
            if tipo_venda in vendas_consolidado:
                vendas_consolidado[tipo_venda] += valor
            else:
                vendas_consolidado[tipo_venda] = valor

print(vendas_consolidado)


## Exercícios com WHILE

"""Exercício 11. Leitura de Dados até Flag
Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida."""

entrada = input("Palavra: ")

while entrada != 'sair':
    entrada = input('Você digitou a palavra errada. Tente novamente: ')


"""Exercício 12. Validação de Entrada
Solicitar ao usuário um número dentro de um intervalo específico até que a entrada 
seja válida."""

numero = None
numero_final = None

while numero == None:
    try:
        numero = int(input('Digite um número de 1 a 5: ').strip())
    except ValueError:
        print('Você digitou o número em formato incorreto. Informe o número inteiro sem vírgulas ou pontos.')
        numero = None

while numero_final == None:
    try:
        while numero > 5 or numero < 1:
            numero = int(input('Número digitado está fora do padrão (1 a 5). Tente novamente: ').strip())
            numero_final = numero
    except ValueError:
        print('Você digitou o número em formato incorreto. Informe o número inteiro sem vírgulas ou pontos.')
        numero_final = None

"""Exercício 13. Consumo de API Simulado
Simular o consumo de uma API paginada, onde cada "página" de dados é processada 
em loop até que não haja mais páginas."""

"""Exercício 14. Tentativas de Conexão
Simular tentativas de reconexão a um serviço com um limite máximo de tentativas."""

"""Exercício 15. Processamento de Dados com Condição de Parada
Processar itens de uma lista até encontrar um valor específico que indica a parada."""
