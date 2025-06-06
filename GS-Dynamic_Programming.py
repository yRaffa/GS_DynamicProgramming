### INTEGRANTES ###

# RM: 556197 - Caio Felipe de Lima Bezerra
# RM: 554736 - Rafael Federici de Oliveira
# RM: 554873 - Sofia Fernandes

### BIBLIOTECAS ###

import pandas as pd # Biblioteca usada para criar e exibir tabelas
from datetime import datetime # Biblioteca para tratar datas

### FUNÇÕES ###

# Função para inputs com validação de opções pré-definidas
def inputOpcoes(msg, opcoes):
    opcoes_str = ' | '.join(opcoes)
    while True:
        escolha = input(f'\nOPÇÕES -> [ {opcoes_str} ]\n\n{msg}')
        if escolha in opcoes:
            return escolha
        print('\n > Opção Inválida!!! \n')

# Função para entrada de valores numéricos do tipo float
def inputNum(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except ValueError:
            print('\n > Você deve digitar um valor numérico!!! \n')

# Função para entrada de valores numéricos do tipo inteiro
def inputInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print('\n > Você deve digitar um valor inteiro!!! \n')

# Função para entrada de datas no formato 'dd/mm/aaaa'
def inputData(msg):
    while True:
        try:
            data = input(msg)
            data = datetime.strptime(data, '%d/%m/%Y') # Converte a string em objeto datetime
            return data.strftime('%d/%m/%Y') # Retorna a data formatada
        except ValueError:
            print('\n > Formato de data invalido!!! \n')

# Função que valida se um valor inserido existe em uma lista de chaves do dicionário
def inputDic(msg, dic, chave):
    while True:
        key = input(msg)
        if key in [str(i) for i in dic[chave]]:
            return key
        print('\n > Digite uma opção existente \n')

# Função que procura e retorna o indice do maior elemento de uma lista
def maiorElementoLista(lista):
    maior = 0
    maior_elemento = lista[maior]
    for i in range(len(lista)):
        if lista[i] > maior_elemento:
            maior_elemento = lista[i]
            maior = i
    return maior

# Função que procura e retorna o indice do menor elemento de uma lista
def menorElementoLista(lista):
    indice_menor = 0
    menor_elemento = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor_elemento:
            menor_elemento = lista[i]
            indice_menor = i
    return indice_menor

# Função de busca binária em uma lista ordenada
# Em comparação ao uso de .index(), que faz uma busca linear O(n), a buscaBinaria() tem uma melhor eficiência O(log n).
def buscaBinaria(lista, num):
    ini = 0
    fim = len(lista) - 1
    while ini <= fim:
        i_chute = (ini + fim) // 2
        chute = lista[i_chute]
        if chute == num:
            return i_chute
        if chute > num:
            fim = i_chute - 1
        else:
            ini = i_chute + 1
    return -1

# Função que exibe o dicionário em formato de tabela usando o pandas
def visualizarTabela(dic):
    df = pd.DataFrame(dic)
    print(f'\n{df.to_string(index = False)}\n')
    return

# Função que adiciona um novo item ao dicionário
def dicAdicionar(dic):
    adicionar_id = max(dic['ID']) + 1 # Gera novo ID automaticamente
    dic['ID'].append(adicionar_id)
    print('\n > ADICIONAR dados de incêndio a tabela: \n')
    for key in tipos.keys(): # Pede os dados conforme os tipos definidos
        adicionar = tipos[key](f'{key}: ')
        dic[key].append(adicionar)
    return

# Função que consulta e exibe os dados de um item do dicionário com base no ID informado
def dicConsultar(dic, chave):
    consultar = inputDic('Digite o ID do incêndio que deseja CONSULTAR: ', dic, chave)
    # indice_consultar = dic[chave].index(int(consultar)) # Notação O Grande: O(n) (menos eficiente)
    indice_consultar = buscaBinaria(dic[chave], int(consultar)) # Notação O Grande: O(log n) (mais eficiente)
    print(f'\n > Informações do incêndio selecionado: \n')
    for key in dic.keys():
        print(key, end = ': ')
        print(dic[key][indice_consultar])
    return

# Função que atualiza os dados de um item do dicionário com base no ID informado
def dicAtualizar(dic, chave):
    atualizar = inputDic('Digite o ID do incêndio que deseja ATUALIZAR: ', dic, chave)
    # indice_atualizar = dic[chave].index(int(atualizar)) # Notação O Grande: O(n) (menos eficiente)
    indice_atualizar = buscaBinaria(dic[chave], int(atualizar)) # Notação O Grande: O(log n) (mais eficiente)
    chaves = list(tipos.keys())
    opcoes_atualizar = list(map(str, range(0, len(chaves) + 1)))
    print('\n > Opcoes de Atualizacoes: \n')
    print('0 - Todos os Dados')
    for i, chave_nome in enumerate(chaves, start = 1):
        print(f'{i} - {chave_nome}')
    tipo_atualizar = inputOpcoes('Quais dados voce quer ATUALIZAR do incêndio selecionado? ', opcoes_atualizar)
    match tipo_atualizar:
        case '0':  # Atualiza todos os campos
            for key in tipos.keys():
                mudanca = tipos[key](f'Atualizar {key}: ')
                dic[key][indice_atualizar] = mudanca
        case _: # Atualiza campos individuais
            chave_atualizar = chaves[int(tipo_atualizar) - 1]
            mudanca = tipos[chave_atualizar](f'Atualizar {chave_atualizar}: ')
            dic[chave_atualizar][indice_atualizar] = mudanca
    return

# Função que exclui os dados de um item do dicionário com base no ID informado
def dicExcluir(dic, chave):
    excluir = inputDic('Digite o ID do incêndio que deseja EXCLUIR: ', dic, chave)
    # indice_excluir = dic[chave].index(int(excluir)) # Notação O Grande: O(n) (menos eficiente)
    indice_excluir = buscaBinaria(dic[chave], int(excluir)) # Notação O Grande: O(log n) (mais eficiente)
    for key in dic.keys():
        dic[key].pop(indice_excluir) # Remove os dados de todas as colunas para esse índice
    return

# Função que busca dados de um item do dicionário com base em filtros
def dicFiltros(dic):
    print('\n > Filtros de Busca: \n\n'
        '1 - Incêndio mais novo \n'
        '2 - Incêndio mais antigo \n'
        '3 - Maior incêndio (km²) \n'
        '4 - Menor incêndio (km²) \n'
        '5 - Último item adicionado')
    opcoes_filtros = ['1', '2', '3', '4', '5']
    filtro = inputOpcoes('Escolha um filtro para busca: ', opcoes_filtros)
    match filtro:
        case '1': # Incêndio mais novo
            datas = [datetime.strptime(data, '%d/%m/%Y') for data in dic['Data Incêndio']]
            indice_filtro = maiorElementoLista(datas)
            nome_filtro = 'Incêndio mais novo'
        case '2':  # Incêndio mais antigo
            datas = [datetime.strptime(data, '%d/%m/%Y') for data in dic['Data Incêndio']]
            indice_filtro = menorElementoLista(datas)
            nome_filtro = 'Incêndio mais antigo'
        case '3': # Maior incêndio
            indice_filtro = maiorElementoLista(dic['Tamanho (km²)'][:])
            nome_filtro = 'Maior incêndio (km²)'
        case '4': # Menor incêndio
            indice_filtro = menorElementoLista(dic['Tamanho (km²)'][:])
            nome_filtro = 'Menor incêndio (km²)'
        case '5': # Último item adicionado
            indice_filtro = maiorElementoLista(dic['ID'][:])
            nome_filtro = 'Último item adicionado'
    print(f'\n > {nome_filtro}: \n')
    for key in dic.keys():
        print(key, end = ': ')
        print(dic[key][indice_filtro])
    return

### VARIÁVEIS GLOBAIS ###

# Dicionário principal com os dados dos incêndios
incendios = {
    'ID' : [],
    'Nome Incêndio' : ['GLO-STICK', 'MARS', 'HUTCHCROFT', 'BENNETTS CORNER FIRE', '826 LEELO COURT'],
    'Data Incêndio' : ['01/09/2003', '28/08/2002', '26/06/2005', '10/10/2003', '19/02/2004'],
    'Data Descoberta' : ['02/09/2003', '28/08/2002', '26/06/2005', '10/10/2003', '20/02/2004'],
    'Data Contenção' : ['03/09/2003', '29/08/2002', '26/06/2005', '12/10/2003', '20/02/2004'],
    'Causa' : ['Natural', 'Natural', 'Humana', 'Humana', 'Humana'],
    'Classificação' : ['A', 'A', 'B', 'A', 'A'],
    'Tamanho (km²)' : [0.15, 0.1, 0.75, 0.01, 0.05],
    'Latitude' : [4237911, 4206309, 4465717, 4440448, 4399677],
    'Longitude' : [-12198978, -1221124, -12374707, -12256454, -1241208],
    'Estado' : ['OR', 'OR', 'OR', 'OR', 'OR']
}

# Preenche o campo ID com valores sequenciais
incendios['ID'] = [i for i, _ in enumerate(incendios['Nome Incêndio'])]

# Dicionário que define qual função de entrada será usada para cada campo
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

# Opções disponíveis no menu principal
opcoes_menu = ['0', '1', '2', '3', '4', '5']

### CODIGO ###

while True: # Laço principal do sistema com menu de navegação
    print('\n----- CodeGreen -----\n\n'
        '1 - ADICIONAR dados de incêndio \n'
        '2 - CONSULTAR dados de incêndio \n'
        '3 - ATUALIZAR dados de incêndio \n'
        '4 - EXCLUIR dados de incêndio \n'
        '5 - BUSCAR dados de incêndio via FILTROS \n'
        '0 - SAIR do sistema')

    # Escolha da opção do menu
    opcao = inputOpcoes('Escolha uma opção: ', opcoes_menu)

    match opcao:
        case '1': # Execução da função adicionar
            dicAdicionar(incendios)
            input('\nDados ADICIONADOS!!!\nPressione qualquer tecla para voltar... ')
        case '2': # Execução da função consultar
            visualizarTabela(incendios)
            dicConsultar(incendios, 'ID')
            input('\nDados CONSULTADOS!!!\nPressione qualquer tecla para voltar... ')
        case '3': # Execução da função atualizar
            visualizarTabela(incendios)
            dicAtualizar(incendios, 'ID')
            input('\nDados ATUALIZADOS!!!\nPressione qualquer tecla para voltar... ')
        case '4': # Execução da função excluir
            visualizarTabela(incendios)
            dicExcluir(incendios, 'ID')
            input('\nDados EXCLUIDOS!!!\nPressione qualquer tecla para voltar... ')
        case '5': # Execução da função buscar via filtros
            dicFiltros(incendios)
            input('\nBUSCA realizada!!!\nPressione qualquer tecla para voltar... ')
        case '0': # Saida do sistema
            print('\n > SISTEMA FECHADO... \n')
            break