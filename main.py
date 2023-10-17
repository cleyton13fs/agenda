agenda = {}

while True:
    print(('--- Agenda telefônica ---'))
    print('1 - adicionar contato')
    print('2- Editar contato (telefone')
    print('3 - Remover contato')
    print('4 - Buscar contato')
    print('5 - listar todos')
    print('6 - sair')
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        agenda[nome] = telefone
        print(('Contato adicionado com sucesso!'))
    elif opcao == 2:
        nome = input('Digite o nome do contato')
        if nome in agenda:
            agenda[nome] = input('Digite o novo telefone')
            print('Telefone alterado com sucesso!')
        else:
            print('Contato não encontrado!')
    elif opcao == 3:
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            del agenda[nome]
            print('Contato removido com sucesso')
        else:
            print('Contato não encontrado')
    elif opcao == 4:
        nome = input('Digite o nome do contato')
        if nome in agenda:
            print(f'Telefone do {nome}: {agenda[nome]}')
        else:
            print('Contato não encontrado!')
    elif opcao == 5:
        print('Todos os contatos')
        for nome in agenda:
            print(f'Nome: {nome} - Telefone: {agenda[nome]}')
    elif opcao == 6:
        break
    else:
        print('Opção inválida')

