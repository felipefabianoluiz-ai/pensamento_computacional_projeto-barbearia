









print("\n=== GESTAO DA BARBEARIA ===")
print("1. Agendar cliente")
print("2. ver agenda")
print("3. mudar servico")
print('4.cancelar agendamento')
print('5.relatorio de serviços realizados')
print('0.sair')

while True:
    escolha = input('digite a opção desejada')
    if escolha == '1':
        print('agendamento de cliente')
    elif escolha == '2':
        print('ver agenda') 
    elif escolha == '3':
        print('mudar serviço')
    elif escolha == '4':
        print('cancelar agendamento')
    elif escolha == '5':
        print('relatorio de serviços realizados')
    elif escolha == '0':
        print('saindo do sistema')
    else:
        print('opção inválida, por favor escolha uma opção válida')
        if escolha == '1': 
            nome_cliente = input('digite o nome do cliente')
            print(f'cliente {nome_cliente} agendado com sucesso!')
sevico = input('digite o serviço desejado')
if servico == 'corte de cabelo':
    print('o valor do corte de cabelo e R$ 30,00')
    horario = input('digite o horário desejado para o corte de cabelo')
    print(f'horário {horario} agendado para o corte de cabelo')
    print(f'cliente {nome_cliente} agendado com sucesso!')
sevico = input('digite o serviço desejado')
if servico == 'corte de cabelo':
    print('o valor do corte de cabelo e R$ 30,00')
    horario = input('digite o horário desejado para o corte de cabelo')
    print(f'horário {horario} agendado para o corte de cabelo') 
elif servico == 'barba':            
    print('o valor da barba e R$ 20,00')
    horario = input('digite o horário desejado para a barba')
    print(f'horário {horario} agendado para a barba')
elif servico == 'corte de cabelo e barba':
    print('o valor do corte de cabelo e barba e R$ 50,00')
    horario = input('digite o horário desejado para o corte de cabelo e barba')
    print(f'horário {horario} agendado para o corte de cabelo e barba')
else:
    print('serviço inválido, por favor escolha um serviço válido')

if escolha == '2':
    print('ver agenda')
    print('agenda vazia, nenhum cliente agendado')      

escolha = input('digite a opção desejada')
if escolha == '3':  
    print('mudar serviço')
    nome_cliente = input('digite o nome do cliente')
    print(f'cliente {nome_cliente} encontrado')
    novo_servico = input('digite o novo serviço desejado')
    if novo_servico == 'corte de cabelo':
        print('o valor do corte de cabelo e R$ 30,00')
        horario = input('digite o horário desejado para o corte de cabelo')
        print(f'horário {horario} agendado para o corte de cabelo') 
    elif novo_servico == 'barba':            
        print('o valor da barba e R$ 20,00')
        horario = input('digite o horário desejado para a barba')
        print(f'horário {horario} agendado para a barba')
    elif novo_servico == 'corte de cabelo e barba':
        print('o valor do corte de cabelo e barba e R$ 50,00')
        horario = input('digite o horário desejado para o corte de cabelo e barba')
        print(f'horário {horario} agendado para o corte de cabelo e barba')
    else:
        print('serviço inválido, por favor escolha um serviço válido')
        escolha = input('digite o nome do barbeiro')
        if escolha == 'barbeiro 1':
            print('barbeiro 1 felipe selecionado')
        elif escolha == 'barbeiro 2':
            print('barbeiro 2 paulo')
        elif escolha == 'barbeiro 3':
            print('barbeiro 3 joão')
        else:
            print('barbeiro inválido, por favor escolha um barbeiro válido')
barbeiro = input('digite o nome do barbeiro')
if barbeiro == 'barbeiro 1':
    print('barbeiro 1 felipe selecionado')
elif barbeiro == 'barbeiro 2':
    print('barbeiro 2 paulo')
elif barbeiro == 'barbeiro 3':
    print('barbeiro 3 joão')
else:
    print('barbeiro inválido, por favor escolha um barbeiro válido')

agenda = []  # Lista para salvar os dados

while True:
    print("\n1. Agendar cliente | 2. Ver agenda | 0. Sair")
    escolha = input('Digite a opção: ')

    if escolha == '1':
        nome = input('Nome do cliente: ')
        servico = input('Serviço (Corte/Barba): ')
        # Aqui você colocaria a lógica dos preços que você já criou
        
        # Salvando na "memória" do programa
        agendamento = {"cliente": nome, "servico": servico}
        agenda.append(agendamento)
        print(f'Agendado com sucesso!')

    elif escolha == '2':
        print("\n=== AGENDA ATUAL ===")
        for item in agenda:
            print(f"Cliente: {item['cliente']} - Serviço: {item['servico']}")

    elif escolha == '0':
        print("Saindo...")
        break # Encerra o loop e sai do programa 
    else:
        print("Opção inválida, tente novamente.")       
        