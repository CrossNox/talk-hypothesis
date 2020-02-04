from code_add import add_numbers


def test_add_numbers_zero_and_zero():
    assert add_numbers(0, 0) == 0


def test_add_numbers_one_and_zero():
    assert add_numbers(1, 0) == 1


def test_add_numbers_zero_and_one():
    assert add_numbers(0, 1) == 0
