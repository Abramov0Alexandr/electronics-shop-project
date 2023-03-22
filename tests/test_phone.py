import pytest
from src.phone import Phone


def test_phone_init(phone):
    assert phone.name == "Xiaomi note turbo s gt"
    assert phone.price == 10_000
    assert phone.quantity == 20
    assert phone.number_of_sim == 4


def test_radd_classes(phone, item):
    assert item + phone == 40


def test_add_classes(phone):
    test_phone_2 = Phone("Pixel", 110_000, 3, 2)
    assert phone + test_phone_2 == 23


def test_phone_repr(phone):
    assert repr(phone) == "Phone('Xiaomi note turbo s gt', 10000, 20, 4)"


def test_failed_add_classes(phone):
    with pytest.raises(TypeError):
        phone + 12
