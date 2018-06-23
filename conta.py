
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __tem_saldo_disponivel(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saca(self, valor):
        if (self.__tem_saldo_disponivel(valor)):
            self.__saldo -= valor
        else:
            print("Você não tem saldo disponível para sacar o valor de {}".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def conta_banco():
        return "001"

    @staticmethod
    def contas_bancos():
        return {'Brasil' : '001', 'Caixa' : '104', 'Bradesco' : '237'}