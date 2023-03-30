from exceptions import exceptions


class GoodsName:

    @classmethod
    def __verify_name(cls, title):
        if not isinstance(title, str):
            raise exceptions.TypeNameException

        if len(title.strip()) == 0:
            raise exceptions.EmptyNameLen

        for i in title.split():
            if len(i) > 10:
                raise exceptions.InvalidNameLength

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
            raise exceptions.InvalidTypePrice
        if price <= 0:
            raise exceptions.NegativePriceException

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
            raise exceptions.InvalidTypeQuantity
        if quantity < 0:
            raise exceptions.InvalidTypeQuantity

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
            raise exceptions.InvalidSimCardType

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__verify_number_of_sim(value)
        setattr(instance, self.name, value)
