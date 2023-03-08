from string import ascii_letters


class GoodsName:

    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    @classmethod
    def __verify_name(cls, name):
        if not isinstance(name, str):
            raise TypeError('Наименование товара должно быть строкового типа')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for letter in name:
            if len(letter.strip(letters)) != 0:
                raise TypeError("Вы можете использовать только буквы")

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__verify_name(value)
        setattr(instance, self.name, value)


class GoodsPrice:
    @classmethod
    def verify_price(cls, price):
        if not isinstance(price, float | int):
            raise TypeError('Цена должна быть указана в виде числа')
        if price <= 0:
            raise ValueError('Цена не может быть отрицательной')

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_price(value)
        setattr(instance, self.name, value)


class GoodsQuantity:
    @classmethod
    def verify_quantity(cls, quantity):
        if not isinstance(quantity, int):
            raise TypeError('Количество товара указывается в виде целого числа')
        if quantity <= 0:
            raise ValueError('Количество товара не может быть отрицательным')

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_quantity(value)
        setattr(instance, self.name, value)

