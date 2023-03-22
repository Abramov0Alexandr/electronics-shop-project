from string import ascii_letters
from exceptions import exceptions


class GoodsName:

    @classmethod
    def __verify_name(cls, title):
        if not isinstance(title, str):
            raise TypeError('Наименование товара должно быть строкового типа')

        if len(title) == 0:
            raise exceptions.InvalidNameLength('Наименование товара не может быть пустой строкой')

        for i in title.split():
            if len(i) > 10:
                raise exceptions.InvalidNameLength('Длина наименования товара превышает 10 символов')

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__verify_name(value)
        setattr(instance, self.name, value)


class GoodsPrice:
    @classmethod
    def __verify_price(cls, price):
        if not isinstance(price, float | int):
            raise exceptions.PriceException('Цена должна быть указана в виде числа')
        if price <= 0:
            raise exceptions.PriceException('Цена не может быть отрицательной')

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__verify_price(value)
        setattr(instance, self.name, value)


class GoodsQuantity:
    @classmethod
    def __verify_quantity(cls, quantity):
        if not isinstance(quantity, int):
            raise exceptions.GoodsException('Количество товара указывается в виде целого числа')
        if quantity <= 0:
            raise exceptions.GoodsException('Количество товара не может быть отрицательным')

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__verify_quantity(value)
        setattr(instance, self.name, value)


class SimCardValue:

    @classmethod
    def __verify_number_of_sim(cls, value: int):
        if not isinstance(value, int) or value <= 0:
            raise exceptions.InvalidSimCardValue('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__verify_number_of_sim(value)
        setattr(instance, self.name, value)
