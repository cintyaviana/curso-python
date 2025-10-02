
# passo 1
class ContaBancaria:
    titular = ""
    saldo = 0.0
    # passo 2

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    # passo 3: definição de um método/função que representa o depósito de valor na conta
    def depositar(self, valor: float):
        if valor <= 0:
            print('Deposito inválido')
        else:
            # aqui, vamos acessar a propriedade saldo e atribuir à ela o valor dado ao parametro valor
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')

    # passo 4: aqui, vamos acessar a propriedade saldo e atribuir à ela o valor dado ao parametro valor
    def sacar(self, valor: float):
        if valor > self.saldo:
            print('Saldo insuficiente!')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso!')

    # passo 5: método/função que representa a consulta de saldo da conta
    def consultar_saldo(self):
        return f'Saldo atual: R${self.saldo:.2f}'


print()
print('Correntista 1')
# passo 6: gerando o objeto
correntista1 = ContaBancaria('Hubert', 10000)
# consultar o saldo inicial
print(correntista1.titular)
print(correntista1.consultar_saldo())
# passo 7: fazer uso do objeto para acessar o método de deposito
correntista1.depositar(2850)
# passo8: consultar o saldo depois do deposito
print(correntista1.consultar_saldo())

correntista1.sacar(12000)
print(correntista1.consultar_saldo())

# ======================================================================================

print()
print('Correntista 2')
correntista2 = ContaBancaria('Vinícius', 23500)
# consultar o saldo inicial
print(correntista2.titular)
print(correntista2.consultar_saldo())
# passo 7: fazer uso do objeto para acessar o método de deposito
correntista2.depositar(28513630)
# passo8: consultar o saldo depois do deposito
print(correntista2.consultar_saldo())

correntista2.sacar(20000)
print(correntista2.consultar_saldo())
