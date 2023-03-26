def test_keyboard_str(keyboard):
    assert str(keyboard) == "Razor Deep Tonus 100"


def test_keyboard_lang(keyboard):
    assert keyboard.language == 'EN'


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
