import pytest

from code_add import add_numbers

data = [(0, 0, 0), (1, 0, 1), (0, 1, 1)]


@pytest.mark.parametrize("n1,n2,expected", data)
def test_add_numbers(n1, n2, expected):
    assert add_numbers(n1, n2) == expected
