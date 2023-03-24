class InvalidNameLength(Exception):
    """Ошибка инициализируется в случае, если название превышает 10 символов
    или состоит из пустой строки"""
    pass


class NameException(Exception):
    """Ошибка инициализируется в случае, если для указания имени применяется
    не строковый тип данных"""
    pass


class PriceException(Exception):
    """Ошибка инициализируется при попытке указать отрицательную цену или
    не числовой тип данных"""
    pass


class GoodsException(Exception):
    """Ошибка инициализируется при попытке указать отрицательное кол-во товара или
    не числовой тип данных"""
    pass


class InvalidSimCardValue(Exception):
    """Ошибка инициализируется при попытке установить отрицательное или нулевое
    кол-во симкард"""
    pass
