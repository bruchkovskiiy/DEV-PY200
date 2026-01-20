from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть целым или вещественным числом")
        if not capacity_volume > 0:
            raise ValueError("Объем стакана должен быть больше нуля")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Занятый объем должен быть целым или вещественным числом")
        if occupied_volume < 0:
            raise ValueError("Занятый объем не должен быть отрицательным")
        if occupied_volume > capacity_volume:
            raise ValueError("Занятый объем не может превышать объем стакана")
        self.occupied_volume = occupied_volume
        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)


if __name__ == "__main__":
    glass1 = Glass(200, 100)
    glass2 = Glass(500, 300)

    try:
        incorrect_glass = Glass(10, 100)  # TODO инициализировать не корректные объекты
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")


