from datetime import datetime, timedelta

class ContaBancaria:
    def __init__(self, agencia, conta, saldo_inicial=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo_inicial
        self.transacoes = []
        self.ultimo_reset = datetime.now()

    def deposito(self, valor):
        if valor >= 0:
            self.saldo += valor
            self.transacoes.append("Depósito: R${:.2f}".format(valor))
            return True
        else:
            return False

    def saque(self, valor):
        hoje = datetime.now()
        if (hoje - self.ultimo_reset).days > 0:
            self.transacoes = []
            self.ultimo_reset = hoje

        if 0 < valor <= 500 and len(self.transacoes) < 3 and valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append("Saque: R${:.2f}".format(valor))
            return True
        elif self.saldo < valor:
            print("Saldo insuficiente para saque")
            return False
        else:
            print("Limite diário de saques atingido ou valor de saque inválido")
            return False

    def extrato(self):
        extrato = "Saldo: R${:.2f}\n".format(self.saldo)
        extrato += "\n".join(self.transacoes)
        return extrato


agencia = input("Digite o número da agência: ")
conta = input("Digite o número da conta: ")

conta_usuario = ContaBancaria(agencia, conta, saldo_inicial=1000)

while True:
    print("\nMenu:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para depósito: "))
        conta_usuario.deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para saque: "))
        if conta_usuario.saldo - valor >= 0:
            conta_usuario.saque(valor)
        else:
            print("Saldo insuficiente para saque")
    elif opcao == "3":
        print(conta_usuario.extrato())
    elif opcao == "0":
        break
    else:
        print("Opção inválida")

print("Obrigado por utilizar nosso sistema!")
