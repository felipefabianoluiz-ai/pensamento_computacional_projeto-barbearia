









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
        