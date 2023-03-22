from descriptors import descriptors
from src.item import Item


class Phone(Item):

    number_of_sim = descriptors.SimCardValue()

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __radd__(self, other):
        self.__verify_classes(other)
        return self.quantity + other.quantity

    def __add__(self, other):
        self.__verify_classes(other)
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @classmethod
    def __verify_classes(cls, other):
        if not isinstance(other, Item | Phone):
            raise TypeError("Действие допустимо только для экземпляров класса Item или Phone")


