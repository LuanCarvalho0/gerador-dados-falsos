from funcoes import *


while True:
    os.system("cls")
    opcoes = iniciar()
    if opcoes == 'parar':
        print(vermelho('Encerrando o programa...'))
        exit()

    dados = gerar_dados_aleatorio(opcoes)
    imprimir_dados_na_tela(dados)

    resposta = input(
        'Gostaria de salvar os dados em um arquivo de texto? [s/n]: ').lower()
    if resposta == 's':
        salvar_dados_em_arquivo_texto(dados)

    input(amarelo('Precione qualquer tecla para continuar...'))
