# **🍃 GS 2025 PROTECH THE FUTURE 🌐**

# 🐍 Dynamic Programing (2ESA)

## 👥 Integrantes
- RM: 556197 // Caio Felipe de Lima Bezerra
- RM: 554736 // Rafael Federici de Oliveira
- RM: 554873 // Sofia Fernandes

## 📕 Sobre o Projeto

🍃 CodeGreen - Sistema de Gerenciamento de Incêndios Florestais

Este sistema foi desenvolvido em [Python](https://www.python.org/doc/) com o objetivo de gerenciar (registrar, visualizar, consultar, atualizar e excluir) informações sobre incêndios florestais. Ele funciona inteiramente via terminal e utiliza estruturas de dados simples (dicionários com listas), além da biblioteca [Pandas](https://pandas.pydata.org/) para exibição organizada dos dados em formato de tabela.

## 🧩 Funcionalidades Principais

**🔸 Adicionar Dados de Incêndio**

Permite o cadastro dos dados de um incêndio.

Solicita os seguintes dados:

- Nome do Incêndio
- Datas (Incêndio, Descoberta, Contenção)
- Causa
- Classificação
- Tamanho (km²)
- Localização (Latitude, Longitude)
- Estado

**🔸 Consultar Dados de Incêndio**

Mostra todos os dados em formato de tabela.

Permite ao usuário selecionar um incêndio pelo seu ID e visualizar suas informações detalhadas.

**🔸 Atualizar Dados de Incêndio**

Permite alterar os dados de um incêndio já registrado.

Pode-se atualizar todos os campos ou apenas um campo específico.

**🔸 Excluir Dados de Incêndio**

Remove completamente um registro selecionado pelo ID.

**🔸 Buscar dados de Incêndio Utilizando Filtros**

Mostra as informações detalhadas de um incêndio selecionado por filtros, como:

- Incêndio Mais Novo
- Incêndio Mais Antigo
- Maior Incêndio (km²)
- Menor Incêndio (km²)
- Último Item Adicionado

**🔸 Sair do Sistema**

Encerra o programa de maneira segura.

## 🧠 Estrutura do Código

**🔹 Funções de Input Personalizado**

Estas funções ajudam a garantir que os dados inseridos estejam no formato correto:

``` inputOpcoes(): ``` Valida opções disponíveis.

``` inputNum(): ``` Garante que seja inserido um número decimal (float).

``` inputInt(): ``` Garante que seja inserido um número inteiro.

``` inputData(): ``` Valida datas no formato dd/mm/aaaa.

``` inputDic(): ``` Valida se a chave (ex: ID) existe no dicionário.

**🔹 Busca Binária**

``` buscaBinaria(): ``` Localiza rapidamente o índice de um ID na lista. A lista deve estar ordenada, como é o caso da lista de IDs.

Em comparação ao uso de ``` .index() ```, que faz uma busca linear **O(n)**, a ``` buscaBinaria() ``` tem uma melhor eficiência **O(log n)**.

**🔹 Busca por Maior e Menor Elemento**

``` maiorElementoLista(): ``` Localiza rapidamente o índice do maior elemento de uma lista.

``` menorElementoLista(): ``` Localiza rapidamente o índice do menor elemento de uma lista.

**🔹 Visualização com Pandas**

``` visualizarTabela(): ``` Converte o dicionário em um DataFrame do [Pandas](https://pandas.pydata.org/) e imprime de forma tabular.

**🔹 Operações com o Dicionário**

Essas funções manipulam os dados principais do sistema:

``` dicAdicionar(): ``` Adiciona novos dados ao dicionário.

``` dicConsultar(): ``` Consulta e exibe dados de um incêndio específico.

``` dicAtualizar(): ``` Permite modificar um ou todos os dados de um incêndio.

``` dicExcluir(): ``` Remove todos os dados de um incêndio selecionado.

``` dicFiltros(): ``` Exibe os dados de um incêndio selecionado por um filtro.

## 📅 Estrutura dos Dados

Os dados dos incêndios são armazenados no dicionário ``` incendios ```, onde cada chave representa um campo (coluna), e os valores são listas (linhas de dados).

Exemplo:

``` python
incendios = {
    'ID': [0, 1, 2],
    'Nome Incêndio': ['FIRE A', 'FIRE B', 'FIRE C'],
    'Data Incêndio': ['dd/mm/aaaa', ...],
    'Data Descoberta' : ['dd/mm/aaaa', ...],
    'Data Contenção' : ['dd/mm/aaaa', ...],
    'Causa' : ['Natural', 'Humana', 'Humana'],
    'Classificação' : ['A', 'A', 'B'],
    'Tamanho (km²)' : [0.1, 0.01, 0.75],
    'Latitude' : [4237911, 4206309, 4465717],
    'Longitude' : [-12198978, -1221124, -12374707],
    'Estado' : ['OR', 'OR', 'OR']
}
```

O campo ``` 'ID' ``` é usado como chave primária para buscas e operações de identificação dos incêndios.

## 📌 Tabela de Tipos

O dicionário ``` tipos ``` define o tipo de input esperado para cada campo:

``` python
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
```

Essa estrutura facilita a reutilização de funções específicas de input ao adicionar ou atualizar dados.

## ▶️ Como Usar

- Execute o código em um terminal Python.
- Um menu será exibido com as opções principais.
- Digite o número da operação desejada.
- Siga as instruções no terminal para preencher ou visualizar os dados.

## ⚠️ Observação

O código utiliza validação básica de entrada, mas não possui persistência de dados. Ao encerrar o programa, os dados são perdidos.
