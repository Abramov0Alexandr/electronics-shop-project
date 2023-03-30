class GoodsTitleException(Exception):
    """Базовый класс исключения для наименования товара"""
    pass


class PriceException(Exception):
    """Базовый класс исключения для указания стоимости товара"""
    pass


class GoodsQuantityException(Exception):
    """Базовый класс исключения для указания количества товара"""
    pass


class SimCardException(Exception):
    """Базовый класс исключения для указания количества Симкарт"""
    pass


class InvalidNameLength(GoodsTitleException):
    """Ошибка инициализируется в случае, если название превышает 10 символов"""
    def __init__(self, *args):
        self.msg = args[0] if args else 'Длина наименования товара превышает 10 символов'

    def __str__(self):
        return self.msg


class EmptyNameLen(GoodsTitleException):
    """Ошибка инициализируется в случае, если название состоит из пустой строки"""
    def __init__(self, *args):
        self.msg = args[0] if args else 'Наименование товара не может быть пустой строкой'

    def __str__(self):
        return self.msg


class TypeNameException(GoodsTitleException):
    """Ошибка инициализируется в случае, если для указания имени применяется
    не строковый тип данных"""
    def __init__(self, *args):
        self.msg = args[0] if args else 'Наименование товара должно быть строкового типа'

    def __str__(self):
        return self.msg


class InvalidTypePrice(PriceException):
    """Ошибка инициализируется при попытке установить нечисловой тип данных"""
    def __init__(self, *args):
        self.msg = args[0] if args else 'Цена должна быть указана в виде числа'

    def __str__(self):
        return self.msg


class NegativePriceException(PriceException):
    """Ошибка инициализируется при попытке указать отрицательную цену товара"""

    def __init__(self, *args):
        self.msg = args[0] if args else 'Цена не может быть отрицательной'

    def __str__(self):
        return self.msg


class InvalidTypeQuantity(GoodsQuantityException):
    """Ошибка инициализируется при попытке указать отрицательное или нечисловое
    количество товара"""
    def __init__(self, *args):
        self.msg = args[0] if args else 'Количество товара указывается в виде целого неотрицательного числа'

    def __str__(self):
        return self.msg


class InvalidSimCardType(SimCardException):
    """Ошибка инициализируется при попытке установить отрицательное или нулевое
    кол-во симкард"""
    def __init__(self,*args):
        self.msg = args[0] if args else 'Количество физических SIM-карт должно быть целым числом больше нуля'

    def __str__(self):
        return self.msg
