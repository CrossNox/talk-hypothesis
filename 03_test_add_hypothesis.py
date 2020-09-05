from hypothesis import given
from hypothesis import strategies as st

from code_add import add_numbers


@given(st.integers(), st.integers())
def test_code_add_commutativity(a, b):
    assert add_numbers(a, b) == add_numbers(b, a)


@given(st.integers())
def test_code_add_identity(a):
    assert add_numbers(a, 0) == a


@given(st.integers(), st.integers(), st.integers())
def test_code_add_associativity(a, b, c):
    assert add_numbers(a, add_numbers(b, c)) == add_numbers(add_numbers(a, b), c)
