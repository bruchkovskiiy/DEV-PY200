import doctest


class Player:
    """
    Представляет аккаунт игрока.
    Класс хранит в себе имя игрока и его уровень, также позволяет его поднимать.
    """

    def __init__(self, player_name: str, player_level: int = 1):
        """
        Инициализирует начальные данные игрока.

        :param player_name: Имя игрока.
        :param player_level: Начальный уровень игрока.

        >>> player = Player("Omenn", 1)  # Инициализация экземпляра класса
        """
        if not isinstance(player_name, str):
            raise TypeError("Имя должно быть типа str")
        self.player_name = player_name

        if not isinstance(player_level, int):
            raise TypeError("Начальный уровень должен быть типа int")
        if player_level < 0:
            raise ValueError("Начальный уровень не может быть отрицательным")
        self.player_level = player_level

    def level_up(self, exp: int) -> str:
        """
        Повышение уровня.

        :param exp: Полученный опыт. Чтобы перейти на следующий, уровень нужно набрать 1000.
        :return: Текущий уровень.

        >>> player = Player("Omenn", 1)
        >>> player.level_up(1000)
        'Уровень игрока: 2'
        """
        if exp >= 0:
            if exp >= 1000:
                self.player_level += 1
                return f"Уровень игрока: {self.player_level}"
            else:
                return "Уровень игрока: 1"
        else:
            raise ValueError("Опыт не может быть отрицательным")

    def get_data(self) -> (str, int):
        """
        Получение данных игрока.

        :return: Данные игрока.

        >>> player = Player("Omenn", 1)
        >>> player.get_data()
        'Имя игрока : Omenn, уровень игрока: 1'
        """
        return f"Имя игрока : {self.player_name}, уровень игрока: {self.player_level}"


if __name__ == "__main__":
    doctest.testmod()