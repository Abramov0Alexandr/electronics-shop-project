import csv
from descriptors import descriptors


CSV_FILE = '../src/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    __pay_rate = 1.0
    all = []

    name = descriptors.GoodsName()
    price = descriptors.GoodsPrice()
    quantity = descriptors.GoodsQuantity()

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.__pay_rate

    @classmethod
    def set_pay_rate(cls, new_rate):

        if 0 <= new_rate:
            cls.__pay_rate = new_rate
        else:
            raise ValueError("Значение индексации не может быть отрицательным или равным '0'")

    @classmethod
    def instantiate_from_csv(cls):
        with open(CSV_FILE) as file:
            file_reader = csv.DictReader(file, delimiter=',')
            for i in file_reader:
                cls.all.append(i)

    @staticmethod
    def string_to_number(any_string: str) -> int:
        try:
            return int(any_string)
        except ValueError:
            return int(any_string[0: any_string.find('.')])
