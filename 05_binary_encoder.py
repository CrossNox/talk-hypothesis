import pytest
from hypothesis import given, reject
from hypothesis import strategies as st


def to_binary(i):
    res = []
    while i != 0:
        i, mod = divmod(i, 2)
        res.append(mod)
    return "".join(map(str, res))[::-1]


def from_binary(b):
    return sum((2 ** idx) * int(v) for idx, v in enumerate(b[::-1]))


@given(st.text(alphabet="1", min_size=1))
def test_only_ones(x):
    assert from_binary(x) == 2 ** len(x) - 1


@given(st.integers(min_value=0))
def test_encode_decode(x):
    assert from_binary(to_binary(x)) == x


@given(st.text(alphabet="01", min_size=1))
def test_decode_encode(x):
    x = x.lstrip("0")
    if len(x) == 0:
        reject()
    assert to_binary(from_binary(x)) == x
