import pytest
import exceptions.exceptions
from src.item import Item


def test_item_init(item):
    assert item.name == "Смартфон"
    assert item.price == 10_000
    assert item.quantity == 20


def test_price_calculation(item):
    assert item.calculate_total_price() == 200_000


def test_discount_calculation(item):
    item.apply_discount()
    assert item.price == 10_000


def test_normal_pay_rate(item):
    Item.set_pay_rate(0.8)
    item.apply_discount()
    assert item.price == 8000.0


def test_str_instance(item):
    assert str(item) == 'Смартфон'


def test_repr_instance(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_negative_pay_rate():
    with pytest.raises(ValueError):
        Item.set_pay_rate(-2)


def test_str_to_num():
    assert Item.string_to_number('9.2') == 9


def test_get_from_cvs_normal():
    Item.instantiate_from_csv(CSV_PATH='./src/items.csv')


def test_unreal_csv_file():
    Item.instantiate_from_csv(CSV_PATH='./src/unreal_file.csv')
    assert 'Отсутствует файл item.csv'


def test_incorrect_csv_file():
    with pytest.raises(exceptions.exceptions.InstantiateCSVError):
        Item.instantiate_from_csv(CSV_PATH='./tests/incorrect_test_file.csv')


def test_normal_add(item):
    test_item = Item('Телефон', 1000, 3)
    assert item + test_item == 23


def test_error_add(item):
    with pytest.raises(TypeError):
        result = item + 10
