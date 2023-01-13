from faker import Faker
import os


##### Funções de utilidade #####

def iniciar():
    print('-=' * 42)
    print('Bem-vindo ao Gerador de Dados de Testes - ' +
          vermelho('Para finalizar o programa, digite "parar"'))
    print('-=' * 42)
    print(
        f'Escolha uma ou mais opções abaixo a serem geradas aleatóriamente: {amarelo("EX -> 1,2,3,4,5")}')
    print('[1] - Nome\n[2] - E-mail\n[3] - Telefone\n[4] - Cidade\n[5] - Estado')
    opcoes = input('Digite uma(as) opções: ')
    print('-=' * 30)
    return opcoes.strip().lower()


def gerar_dados_aleatorio(opcoes):

    fake = Faker('pt-BR')

    opcoes = opcoes.split(',')
    lista_dados = []
    for opcao in opcoes:
        if opcao == '1':
            lista_dados.append(fake.name())
        elif opcao == '2':
            lista_dados.append(fake.email())
        elif opcao == '3':
            lista_dados.append(fake.phone_number())
        elif opcao == '4':
            lista_dados.append(fake.city())
        elif opcao == '5':
            lista_dados.append(fake.state())

    return lista_dados


def salvar_dados_em_arquivo_texto(dados):
    with open('dados.txt', 'a+', newline='') as arquivo:
        for dado in dados:
            arquivo.write(dado + os.linesep)


def imprimir_dados_na_tela(dados):
    print('-' * 30)
    print('\tDADOS GERADOS')
    print('-' * 30)
    for dado in dados:
        print(verde(dado))
    print('-=' * 30)


##### Funções de Colorir #####

def vermelho(texto):
    return f'\033[31m{texto}\033[0;0m'


def verde(texto):
    return f'\033[32m{texto}\033[0;0m'


def amarelo(texto):
    return f'\033[33m{texto}\033[0;0m'
