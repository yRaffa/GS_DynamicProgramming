### BIBLIOTECAS ###

import pandas as pd
from datetime import datetime

### FUNÇÕES ###

# Função para inputs com opções pré-cadastradas
def inputOpcoes(msg, opcoes):
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

# Função para inputs especificos de datas
def inputData(msg):
    while True:
        try:
            data = input(msg)
            data = datetime.strptime(data, '%d/%m/%Y')
            return data.strftime('%d/%m/%Y')
        except ValueError:
            print('\n > Formato de data invalido!!! \n')

# Função para inputs de indices de dicionarios
def inputDic(msg, dic, chave):
    while True:
        key = input(msg)
        if key in [str(i) for i in dic[chave]]:
            return key
        print('\n > Digite uma opção existente \n')

# Função para mostrar tabela
def visualizarTabela(dic):
    df = pd.DataFrame(dic)
    print(f'\n{df.to_string(index = False)}\n')
    return

# Função que adiciona um item a um dicionario de listas (ultimo indice)
def dicAdicionar(dic):
    adicionar_id = max(dic['ID']) + 1
    dic['ID'].append(adicionar_id)
    print('\n > ADICIONAR dados de incêndio a tabela: \n')
    for key in tipos.keys():
        adicionar = tipos[key](f'{key}: ')
        dic[key].append(adicionar)
    return

# Função que consulta os dados de um item de um dicionario, atravez do indice
def dicConsultar(dic, chave):
    consultar = inputDic('Digite o ID do incendio que deseja CONSULTAR: ', dic, chave)
    indice_consultar = dic['ID'].index(int(consultar))
    print(f'\n > Informações do incendio selecionado: \n')
    for key in dic.keys():
        print(key, end = ': ')
        print(dic[key][indice_consultar])
    return

# Função que atualiza os dados de um item de um dicionario, atravez do indice
def dicAtualizar(dic, chave):
    atualizar = inputDic('Digite o ID do incendio que deseja ATUALIZAR: ', dic, chave)
    indice_atualizar = dic['ID'].index(int(atualizar))
    chaves = list(tipos.keys())
    opcoes_atualizar = list(map(str, range(0, len(chaves) + 1)))
    print('\n > Opcoes de Atualizacoes: \n')
    print('0 - Todos os Dados')
    for i, chave_nome in enumerate(chaves, start = 1):
        print(f'{i} - {chave_nome}')
    tipo_atualizar = inputOpcoes('Quais dados voce quer ATUALIZAR do incendio selecionado? ', opcoes_atualizar)
    match tipo_atualizar:
        case '0':
            for key in tipos.keys():
                mudanca = tipos[key](f'Atualizar {key}: ')
                dic[key][indice_atualizar] = mudanca
        case _:
            chave_atualizar = chaves[int(tipo_atualizar) - 1]
            mudanca = tipos[chave_atualizar](f'Atualizar {chave_atualizar}: ')
            dic[chave_atualizar][indice_atualizar] = mudanca
    return

# Função que exclui os dados de um item de um dicionario, atravez do indice
def dicExcluir(dic, chave):
    excluir = inputDic('Digite o ID do incendio que deseja EXCLUIR: ', dic, chave)
    indice_excluir = dic['ID'].index(int(excluir))
    for key in dic.keys():
        dic[key].pop(indice_excluir)
    return

### VARIÁVEIS GLOBAIS ###

incendios = {
    'ID' : [],
    'Nome Incêndio' : ['GLO-STICK', 'MARS', 'HUTCHCROFT', 'BENNETTS CORNER FIRE', '826 LEELO COURT'],
    'Data Incêndio' : ['28/08/2003', '28/08/2003', '30/08/2003', '01/09/2003', '26/08/2003'],
    'Data Descoberta' : ['28/08/2003', '28/08/2003', '30/08/2003', '01/09/2003', '26/08/2003'],
    'Data Contenção' : ['28/08/2003', '28/08/2003', '30/08/2003', '01/09/2003', '26/08/2003'],
    'Causa' : ['Natural', 'Natural', 'Humana', 'Humana', 'Humana'],
    'Classificação' : ['A', 'A', 'B', 'A', 'A'],
    'Tamanho (km²)' : [0.1, 0.01, 0.75, 0.01, 0.01],
    'Latitude' : [4237911, 4206309, 4465717, 4440448, 4399677],
    'Longitude' : [-12198978, -1221124, -12374707, -12256454, -1241208],
    'Estado' : ['OR', 'OR', 'OR', 'OR', 'OR']
}

incendios['ID'] = [i for i, _ in enumerate(incendios['Nome Incêndio'])]

tipos = {
    'Nome Incêndio' : input,
    'Data Incêndio' : inputData,
    'Data Descoberta' : inputData,
    'Data Contenção' : inputData,
    'Causa' : input,
    'Classificação' : input,
    'Tamanho (km²)' : inputNum,
    'Latitude' : inputInt,
    'Longitude' : inputInt,
    'Estado' : input
}

opcoes_menu = ['0', '1', '2', '3', '4']

### CODIGO ###

while True:
    print('\n----- CodeGreen -----\n\n'
        '1 - ADICIONAR dados de incêndio \n'
        '2 - CONSULTAR dados de incêndio \n'
        '3 - ATUALIZAR dados de incêndio \n'
        '4 - EXCLUIR dados de incêndio \n'
        '0 - SAIR do sistema')

    opcao = inputOpcoes('Digite a opção desejada: ', opcoes_menu)

    match opcao:
        case '1':
            dicAdicionar(incendios)
            input('\nDados ADICIONADOS!!!\nPressione qualquer tecla para voltar... ')
        case '2':
            visualizarTabela(incendios)
            dicConsultar(incendios, 'ID')
            input('\nDados CONSULTADOS!!!\nPressione qualquer tecla para voltar... ')
        case '3':
            visualizarTabela(incendios)
            dicAtualizar(incendios, 'ID')
            input('\nDados ATUALIZADOS!!!\nPressione qualquer tecla para voltar... ')
        case '4':
            visualizarTabela(incendios)
            dicExcluir(incendios, 'ID')
            input('\nDados EXCLUIDOS!!!\nPressione qualquer tecla para voltar... ')
        case '0':
            print('\n > SISTEMA FECHADO... \n')
            break