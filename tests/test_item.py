import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


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


def test_get_from_cvs():
    Item.instantiate_from_csv(CSV_PATH='./src/items.csv')

