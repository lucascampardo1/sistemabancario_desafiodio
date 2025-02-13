menu = """"
    [D] - Depositar
    [S] - Sacar
    [E] - Extrato
    [Q] - Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.upper() == "D":
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: {valor:.2f}\n'
            print('Depósito realizado com sucesso!')

        else:
            print('Valor inválido')

    elif opcao.upper() == "S":
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES

        if valor <= 0:
            print('Valor inválido!')
        elif excedeu_saldo:
            print('Saldo insuficiente!')
        elif excedeu_limite:
            print('Valor acima do limite permitido!')
        elif excedeu_limite_saques:
            print('Limite de saques atingido!')
        else:
            saldo -= valor
            extrato += f'Saque: {valor:.2f}\n'
            numero_saques += 1
            print('Saque realizado com sucesso!')

    elif opcao.upper() == "E":
        print('\n========== Extrato ==========\n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: {saldo:.2f}')
        print(f'Limite por saque: {limite:.2f}')
        print(f'Saques realizados: {numero_saques}')
        print('\n=============================\n')

    elif opcao.upper() == "Q":
        print('Até mais')
        break

    else:
        print('Opção não encontrada!')

