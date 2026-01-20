import doctest


class BankAccount:
    """
    Представляет банковский счет клиента.
    Класс управляет балансом счета, позволяя вносить и снимать средства.
    """

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        """
        Инициализирует новый банковский счет.

        :param account_holder: Имя владельца счета.
        :param initial_balance: Начальный баланс счета.

        >>> account = BankAccount("Tom", 10000.0)  # Инициализация экземпляра класса
        """
        if not isinstance(account_holder, str):
            raise TypeError("Имя владельца должно быть типа str")
        self.account_holder = account_holder

        if not isinstance(initial_balance, float):
            raise TypeError("Начальный баланс должен быть типа float")
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.initial_balance = initial_balance

    def deposit(self, amount: float) -> str:
        """
        Вносит деньги на счет.

        :param amount: Сумма для внесения. Должна быть положительным числом.
        :return: Сообщение о результате операции.

        >>> account = BankAccount("Tom", 10000.0)
        >>> account.deposit(5000.0)
        'Внесено 5000.00 руб. Текущий баланс: 15000.00 руб.'
        """
        if amount > 0:
            self.initial_balance += amount
            return f"Внесено {amount:.2f} руб. Текущий баланс: {self.initial_balance:.2f} руб."
        else:
            raise ValueError("Сумма взноса должна быть положительной")

    def get_balance(self) -> float:
        """
        Возвращает текущий баланс счета.

        :return: Текущий баланс.

        >>> account = BankAccount("Tom", 15000.0)
        >>> account.get_balance()
        15000.0
        """
        return self.initial_balance


if __name__ == "__main__":
    doctest.testmod()