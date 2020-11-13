import json
import sys

import requests


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta:
            return resposta.text
    except Exception as error:
        print(f'Erro ao fazer requisição: {error}')


def parsing(texto_da_resposta):
    try:
        texto_depois_do_parsing = json.loads(texto_da_resposta)
        if texto_depois_do_parsing:
            return texto_depois_do_parsing
    except Exception as error:
        print(f'Erro ao fazer o parsing: {error}')


def mostrar_populacao(nome_do_pais):
    resposta = requisicao(URL_NAME + nome_do_pais)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print(f'{pais["name"]}: {pais["population"]} habitantes.')

        else:
            print('Erro! País não encontrado...')


def mostrar_moedas(nome_do_pais):
    resposta = requisicao(URL_NAME + nome_do_pais)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            print('************************')
            for pais in lista_de_paises:
                print(f'Moedas do país {pais["name"]}:')
                moedas = pais['currencies']
                for moeda in moedas:
                    print(f'{moeda["name"]} - {moeda["code"]}')
            print('************************')
        else:
            print('Erro! País não encontrado...')


def listar_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        paises = parsing(resposta)
        if paises:
            for pais in paises:
                print(pais['name'])


if __name__ == "__main__":

    URL_ALL = "https://restcountries.eu/rest/v2/all"
    URL_NAME = "https://restcountries.eu/rest/v2/name/"

    if len(sys.argv) == 1:
        print(">>> Bem-vindo a Lista de Países!!")
        print('Temos aqui informações sobre 250 países pelo mundo.')
        print('Uso: python paises.py <ação> <nome_do_país>')
        print('Ações disponíveis: nomes, moeda, população')
        print('=-'*25)
    else:
        if len(sys.argv) == 2:
            argumento1 = sys.argv[1]
            if argumento1 == 'nomes':
                listar_paises()
            else:
                print('Argumento inválido!')
        elif len(sys.argv) == 3:
            argumento1 = sys.argv[1]
            argumento2 = sys.argv[2]
            if argumento1 == 'moeda':
                mostrar_moedas(argumento2)
            elif argumento1 == 'população':
                mostrar_populacao(argumento2)
            else:
                print('Algum argumento inválido...')
        else:
            print('Muitos argumentos no terminal.')
