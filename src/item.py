from descriptors import descriptors


class Item:
    """
    Класс для представления товара в магазине.
    """
    __pay_rate = 1.0
    all = []

    name = descriptors.GoodsName()
    price = descriptors.GoodsPrice()
    quantity = descriptors.GoodsQuantity()

    @classmethod
    def set_pay_rate(cls, new_rate):

        if 0 <= cls.__pay_rate:
            cls.__pay_rate = new_rate
        else:
            raise ValueError("Значение индексации не может быть отрицательным или равным '0'")

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
