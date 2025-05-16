import textwrap


def validar_entrada(valor):
    return float(valor.replace(",", "."))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
        print("\n====== Depósito realizado com sucesso! ======")
    else:
        print("\n***** Operação falhou! O valor informado é inválido. *****")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saque = numero_saques >= limite_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite

    if excedeu_saque:
        print("\n***** Operação falhou! Número máximo de saques excedido. *****")

    elif excedeu_saldo:
        print("\n***** Operação falhou! Você não tem saldo suficiente. *****")

    elif excedeu_limite:
        print("\n***** Operação falhou! O valor excedeu o limite permitido por saque. *****")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n====== Saque realizado com sucesso! ======")
    else:
        print("\n***** Operação falhou! O valor informado é inválido. *****")

    return saldo, extrato


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n***** Já existe usuário com esse CPF! *****")
        return

    nome = input("Informe o nome completo: ").title().strip()
    data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n========= Usuário criado com sucesso! =========")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n======= Conta criada com sucesso! =======")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n***** Usuário não encontrado, fluxo de crxiação de conta encerrado! *****")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
         """
        print("*" * 50)
        print(textwrap.dedent(linha))


def exibir_extrato(saldo, /, *, extrato):
    print(" Extrato ".center(45, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("".center(45, "="))


def menu():
    menu = """\n
    ===================== MENU =====================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
    ==> """
    return int(input(textwrap.dedent(menu)))


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 5
    AGENCIA = "0001"
    usuarios = []
    contas = []
    numero_conta = 0

    while True:
        try:
            opcao = menu()

            if opcao == 1:
                valor = validar_entrada(input("Informe o valor que deseja depositar: "))

                saldo, extrato = depositar(saldo, valor, extrato)
            elif opcao == 2:
                valor = validar_entrada(input("Informe o valor que deseja sacar: "))

                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
            elif opcao == 3:
                exibir_extrato(saldo, extrato=extrato)

            elif opcao == 4:
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)

            elif opcao == 5:
                listar_contas(contas)

            elif opcao == 6:
                criar_usuario(usuarios)

            elif opcao == 7:
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida! Por favor, selecione novamente a operação desejada.")
        except KeyboardInterrupt:
            print("\nEncerrado pelo usuário.")
            break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")


main()
