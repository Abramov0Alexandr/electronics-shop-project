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


