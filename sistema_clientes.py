import os

ARQ = 'clientes.txt'  # arquivo de dados

def cadastrar_cliente():
    """Cadastra um novo cliente no arquivo"""
    while True:
        nome = input('Digite o nome: ').strip()
        email = input('Digite o email: ').strip()
        telefone = input('Digite o telefone: ').strip()

        # Validação básica dos campos
        if not nome or not email or not telefone or '@' not in email:
            print('Dados inválidos. Tente novamente.\n')
            continue

        # Gravação em modo append (não sobrescreve os existentes)
        with open(ARQ, 'a') as arq:
            arq.write(f'{nome} - {email} - {telefone}\n')

        print('Cliente cadastrado com sucesso!\n')
        return  # encerra a função e retorna ao menu

def listar_clientes():
    """Lista todos os clientes cadastrados"""
    if not os.path.exists(ARQ) or os.path.getsize(ARQ) == 0:
        print("Não existem clientes cadastrados.\nSelecione a opção '1' para cadastrar o primeiro.\n")
        return

    print('=== Sistema de Clientes ===\nClientes cadastrados:\n')
    with open(ARQ, 'r') as arq:
        for cliente in arq:
            print(cliente.strip())  # .strip() remove o \n no final
    print()

def buscar_cliente():
    """Busca clientes pelo nome (case-insensitive, busca parcial)"""
    if not os.path.exists(ARQ) or os.path.getsize(ARQ) == 0:
        print("Não existem clientes cadastrados.\n")
        return

    nome = input('Pesquisar nome do cliente: ').strip().lower()

    with open(ARQ, 'r') as arq:
        encontrados = [linha.strip() for linha in arq if nome in linha.lower()]

    if encontrados:
        print("\nResultados da busca:")
        for cliente in encontrados:
            print(cliente)
        print()
    else:
        print('Cliente não encontrado. Para cadastrá-lo, selecione a opção 1.\n')

def excluir_cliente():
    """Exclui cliente pelo nome (busca exata)"""
    if not os.path.exists(ARQ) or os.path.getsize(ARQ) == 0:
        print("Não existem clientes cadastrados.\n")
        return

    drop_nome = input('Digite o nome do cliente que deseja excluir: ').strip()
    cadastros = []
    removido = False

    with open(ARQ, 'r') as arq:
        for cliente in arq:
            nome_cliente = cliente.split(" - ", 1)[0].strip()
            if drop_nome == nome_cliente:
                removido = True
            else:
                cadastros.append(cliente)

    if removido:
        with open(ARQ, 'w') as arq:
            arq.writelines(cadastros)
        print('Cliente removido com sucesso\n')
    else:
        print('Cliente não encontrado\n')

def menu():
    """Menu principal"""
    while True:
        print('=== Sistema de Clientes ===')
        print('1 - Cadastrar cliente')
        print('2 - Listar clientes')
        print('3 - Buscar cliente')
        print('4 - Excluir cliente')
        print('5 - Sair')
        escolha = input('Escolha: ').strip()

        if escolha == '1':
            cadastrar_cliente()
        elif escolha == '2':
            listar_clientes()
        elif escolha == '3':
            buscar_cliente()
        elif escolha == '4':
            excluir_cliente()
        elif escolha == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida!\n')

if __name__ == '__main__':
    menu()
