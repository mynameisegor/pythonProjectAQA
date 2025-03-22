class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: int):
        if amount > 0:
            self._balance += amount
            print(f'Баланс пополнен на сумму: {amount}.')
        else:
            raise ValueError("Сумма должна быть положительной")

    def withdraw(self, amount: int):
        if self._balance >= amount:
            self._balance -= amount
            print(f'С баланса снято: {amount}')
        else:
            raise ValueError("Недостаточно средств на балансе.")

    def get_balance(self)-> int:
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.__interest_rate = interest_rate

    def apply_interest(self):
        bonus = self._balance * self.__interest_rate
        self._balance += bonus
        print(f'На счет начислены проценты в размере: {bonus}')


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount: int):
        dept = amount - self._balance
        if self._balance >= amount:
            self._balance -= amount
            print(f'С баланса снято: {amount}')
        else:
            self._balance -= amount
            print(f'С баланса снято: {amount}. Вы взяли в долг {dept}.')


# account = SavingsAccount("Bob", 52)
# account.deposit(500)
# account.apply_interest()
# print(account.get_balance())
# account.withdraw(100)
# print(account.get_balance())


def test_check_balance(dep=500):
    """Проверка корректности работы методов классов"""
    account = SavingsAccount("Matrin", 0)
    account.deposit(dep)
    account.apply_interest()
    account.withdraw(dep)
    balance = account.get_balance()
    assert balance > 0