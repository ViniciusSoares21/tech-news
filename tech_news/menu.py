import sys


# Requisitos 11 e 12
def analyzer_menu():
    value = input("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
""")
    verify = value in ['1', '2', '3', '4', '5']
    if not verify:
        return sys.stderr.write("Opção inválida")
    option = {
        '0': "Digite quantas notícias serão buscadas:",
        '1': "Digite o título:",
        '2': "Digite a data no formato aaaa-mm-dd:",
        '3': "Digite a categoria:",
        '5': 'Encerrando script'
    }
    sys.stdout.write(option[value])
