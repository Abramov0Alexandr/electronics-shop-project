from string import ascii_letters
from exceptions import exceptions


class GoodsName:

    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    @classmethod
    def __verify_name(cls, title):
        if not isinstance(title, str):
            raise TypeError('Наименование товара должно быть строкового типа')
        if len(title) > 10:
            raise exceptions.InvalidNameLength('Длина наименования товара превышает 10 символов')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for letter in title:
            if len(letter.strip(letters)) != 0:
                raise exceptions.NameException("Вы можете использовать только буквы")

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

