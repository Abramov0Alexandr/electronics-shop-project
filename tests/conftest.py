import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone():
    return Phone("Xiaomi note turbo s gt", 10_000, 20, 4)


@pytest.fixture
def keyboard():
    return KeyBoard("Razor Deep Tonus 100", 1337, 4)
