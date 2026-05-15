class BankAccount:
    __slots__ = ('balance',)

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Счет пополнен на {amount}. Текущий баланс: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print(f"Ошибка: Недостаточно средств для снятия {amount}. Баланс: {self.balance}")
        else:
            self.balance -= amount
            print(f"Успешно снято {amount}. Текущий баланс: {self.balance}")

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(200)
acc.withdraw(100)
