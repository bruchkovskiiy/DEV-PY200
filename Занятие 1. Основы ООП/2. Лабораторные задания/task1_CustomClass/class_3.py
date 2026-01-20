import doctest


class HeightAndWeightChart:
    """
    Мой индекс массы тела.
    Класс хранит в себе возраст, рост и вес, а также позволяет определить является ли вес нормальным.
    """

    def __init__(self, age = 25, height = 174, weight = 68):
        """
        Инициализирует рост и вес.

        :param age: Возраст.
        :param height: Вес.
        :param weight: Рост.

        >>> my_parameters = HeightAndWeightChart(25, 174, 68)  # Инициализация экземпляра класса
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

        if not isinstance(height, int):
            raise TypeError("Рост должен быть типа int")
        if height < 0:
            raise ValueError("Рост не может быть отрицательным")
        self.height = height

        if not isinstance(weight, int):
            raise TypeError("Вес должен быть типа int")
        if weight < 0:
            raise ValueError("Вес не может быть отрицательным")
        self.weight = weight

    def body_mass_index(self, weight: int) -> str:
        """
        Определяет нормальный ли вес.

        :param weight: Имеющийся вес.
        :return: Заключение о весе.

        >>> my_parameters = HeightAndWeightChart(25, 174, 68)
        >>> my_parameters.body_mass_index(68)
        'Нормальный вес'
        """
        if 64 < weight < 74:
            return "Нормальный вес"
        else:
            return "Вес за пределами нормы"

    def get_data(self) -> int:
        """
        Получение данных роста и веса.

        :return: Мои параметры.

        >>> my_parameters = HeightAndWeightChart(25, 174, 68)
        >>> my_parameters.get_data()
        'Возраст: 25, рост: 174, вес: 68'
        """
        return f"Возраст: {self.age}, рост: {self.height}, вес: {self.weight}"


if __name__ == "__main__":
    doctest.testmod()