import os
from heaplib import HeapMin

controller = HeapMin(fila_prioridade=[], fila_atendidos=[])

while True:
    print("\nMenu:")
    print("1. Atender paciente de maior prioridade")
    print("2. Mostrar fila de pacientes")
    print("3. Mostrar próximo paciente")
    print("4. Listar 5 últimos pacientes atendidos")
    print("5. Listar todos os pacientes atendidos")
    print("6. Sair")

    opcao = input("Escolha uma opção (1-6): ")
    if not controller.fila_prioridade:
        controller.fila_prioridade = [(1, 1, 'Ana'), (22, 2,'Maria'), (33, 3,'Pedro'), (1, 4, 'Ana'), (5, 5, 'Lucas'), (6, 6, 'Clara'), (1, 2, 'Ana', (1, 5, 'Ana'))]
        controller.heapify(controller.fila_prioridade)

    if opcao == '1':
        os.system('clear')
        controller.pop()

    elif opcao == '2':
        os.system('clear')
        controller.printPriority()

    elif opcao == '3':
        os.system('clear')
        controller.printNext()

    elif opcao == '4':
        os.system('clear')
        controller.printServed()

    elif opcao == '5':
        os.system('clear')
        controller.printServed(showJustFive = False)

    elif opcao == '6':
        print("Saindo do jogo. Até logo!")
        break

    else:
        os.system('clear')
        print("Opção inválida. Escolha novamente.")