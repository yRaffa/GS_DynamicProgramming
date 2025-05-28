###################
### BIBLIOTECAS ###
###################

import pandas as pd
from datetime import datetime

###############
### FUNÇÕES ###
###############

# Função para inputs com opções pré-cadastradas
def inputValido(msg, opcoes):
    opcoes_str = ' | '.join(opcoes)
    while True:
        escolha = input(f'\nOPÇÕES -> [ {opcoes_str} ]\n\n{msg}')
        if escolha in opcoes:
            return escolha
        print('\n > Opção Inválida!!! \n')

# Função para inputs especificos de valores numericos (float)
def inputNum(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except ValueError:
            print('\n > Você deve digitar um valor numérico!!! \n')

# Função para inputs especificos de valores numericos (int)
def inputInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print('\n > Você deve digitar um valor inteiro!!! \n')

# Função para input especifico de datas
def inputData(msg):
    while True:
        data = input(msg)
        try:
            data = datetime.strptime(data, '%d/%m/%Y')
            return data.strftime('%d/%m/%Y')
        except ValueError:
            print('\n > Formato de data invalido!!! \n')

# Função para mostrar tabela
def verTabela(dic):
    tabela = pd.DataFrame(dic)
    print('\nRELATORIOS: ')
    print(f'\n{tabela}\n')
    return

# Printa um dicionario de forma identada
def printDic(dic, level = 0):
    for key in dic.keys():
        if type(dic[key]) is not dict:
            print(f'{level * "  "}{key}: {dic[key]}')
        else:
            level += 2
            print(f'{key}:')
            printDic(dic[key], level)
            level -= 2

# Cria um dicionario com os indices de uma lista que são valores de outro dicionario
def dicIndices(dic, chave):
    indices = {}
    for i in range(len(dic[chave])):
        indices[dic[chave][i]] = i
    return indices

#########################
### VARIÁVEIS GLOBAIS ###
#########################

incendios = {
    'ID' : [0, 1, 2, 3, 4],
    'Nome Incendio' : ['GLO-STICK', 'MARS', 'HUTCHCROFT', 'BENNETTS CORNER FIRE', '826 LEELO COURT'],
    'Data Incendio' : ['28/08/2003', '28/08/2003', '30/08/2003', '01/09/2003', '26/08/2003'],
    'Data Descoberta' : ['28/08/2003', '28/08/2003', '30/08/2003', '01/09/2003', '26/08/2003'],
    'Data Contencao' : ['28/08/2003', '28/08/2003', '30/08/2003', '01/09/2003', '26/08/2003'],
    'Causa' : ['Natural', 'Natural', 'Humana', 'Humana', 'Humana'],
    'Tamanho Incendio Classificacao' : ['A', 'A', 'B', 'A', 'A'],
    'Tamanho Incendio' : [0.1, 0.01, 0.75, 0.01, 0.01],
    'Latitude' : [4237911, 4206309, 4465717, 4440448, 4399677],
    'Longitude' : [-12198978, -1221124, -12374707, -12256454, -1241208],
    'Estado' : ['OR', 'OR', 'OR', 'OR', 'OR']
}

tipos = {
    'ID' : inputInt,
    'Nome Incendio' : input,
    'Data Incendio' : inputData,
    'Data Descoberta' : inputData,
    'Data Contencao' : inputData,
    'Causa Classificacao' : input,
    'Causa Geral' : input,
    'Tamanho Incendio Classificacao' : input,
    'Tamanho Incendio' : inputNum,
    'Latitude' : inputNum,
    'Longitude' : inputNum,
    'Estado' : input
}

ids = dicIndices(incendios, 'Nome Incendio')

opcoes_menu = '012345'

##############
### TESTES ###
##############

while True:
    print('\n----- CodeGreen -----\n\n'
        '1. Visualizar Tabela \n'
        '2. Consultar um Incendio \n'
        '3. Adicionar uma Entrada de Incendio \n'
        '4. Atualizar uma Entrada de Incendio \n'
        '5. Remover uma Entrada de Incendio \n'
        '0. Sair')

    opcao = inputValido('Digite a opção desejada: ', opcoes_menu)

    match opcao:
        case 1:
        
        # case 2:

        # case 3:

        # case 4:

        # case 5:

        case 0:
            print('\n > FECHANDO SISTEMA... \n')
            break

'''
data = inputData('Data (dd/mm/aaaa): ')
print(data)
print(type(data))
'''

verTabela(incendios)