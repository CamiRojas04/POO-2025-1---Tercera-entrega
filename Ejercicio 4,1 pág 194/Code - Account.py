#Ejercicio 4,1 - Página 194

class Account:
    def __init__(self, balance: float, annual_rate: float):
        self._balance = balance                  # saldo actual
        self._annual_rate = annual_rate          # tasa anual
        self._monthly_fee = 0.0                  # comisión mensual
        self._num_deposits = 0                   # número de consignaciones
        self._num_withdrawals = 0                # número de retiros

    def deposit(self, amount: float):
        self._balance += amount
        self._num_deposits += 1

    def withdraw(self, amount: float):
        if self._balance >= amount:
            self._balance -= amount
            self._num_withdrawals += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calculate_interest(self):
        monthly_rate = self._annual_rate / 12
        monthly_interest = self._balance * monthly_rate
        self._balance += monthly_interest

    def monthly_statement(self):
        self._balance -= self._monthly_fee
        self.calculate_interest()

    def print_statement(self):
        print(f"Saldo = ${self._balance:.2f}")
        print(f"Comisión mensual = ${self._monthly_fee:.2f}")
        print(f"Número de transacciones = {self._num_deposits + self._num_withdrawals}\n")


class SavingsAccount(Account):
    def __init__(self, balance: float, annual_rate: float):
        super().__init__(balance, annual_rate)

    def _is_active(self):
        return self._balance >= 10000

    def deposit(self, amount: float):
        if self._is_active():
            super().deposit(amount)
        else:
            print("Cuenta inactiva: no se pueden hacer consignaciones.")

    def withdraw(self, amount: float):
        if self._is_active():
            super().withdraw(amount)
        else:
            print("Cuenta inactiva: no se pueden hacer retiros.")

    def monthly_statement(self):
        if self._num_withdrawals > 4:
            extra_fee = (self._num_withdrawals - 4) * 1000
            self._monthly_fee += extra_fee
        super().monthly_statement()

    def print_statement(self):
        super().print_statement()


class CheckingAccount(Account):
    def __init__(self, balance: float, annual_rate: float):
        super().__init__(balance, annual_rate)
        self._overdraft = 0.0

    def withdraw(self, amount: float):
        potential_balance = self._balance - amount
        if potential_balance < 0:
            self._overdraft -= potential_balance  # potencial_balance negativo, resta aumenta sobregiro
            self._balance = 0
        else:
            super().withdraw(amount)

    def deposit(self, amount: float):
        if self._overdraft > 0:
            remaining_overdraft = self._overdraft - amount
            if remaining_overdraft > 0:
                self._overdraft = remaining_overdraft
            else:
                self._overdraft = 0
                self._balance = -remaining_overdraft  # si sobra dinero después de pagar sobregiro
        else:
            super().deposit(amount)

    def print_statement(self):
        print(f"Saldo = ${self._balance:.2f}")
        print(f"Comisión mensual = ${self._monthly_fee:.2f}")
        print(f"Número de transacciones = {self._num_deposits + self._num_withdrawals}")
        print(f"Valor de sobregiro = ${self._overdraft:.2f}\n")


if __name__ == "__main__":
    print("Cuenta de Ahorros")
    initial_balance = float(input("Ingrese saldo inicial: $"))
    annual_rate = float(input("Ingrese tasa de interés (decimal, ej: 0.015): "))
    account = SavingsAccount(initial_balance, annual_rate)
    deposit_amount = float(input("Ingresar cantidad a consignar: $"))
    account.deposit(deposit_amount)
    withdraw_amount = float(input("Ingresar cantidad a retirar: $"))
    account.withdraw(withdraw_amount)
    account.monthly_statement()
    account.print_statement()
