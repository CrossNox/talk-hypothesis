# https://www.youtube.com/watch?v=jvwfDdgg93E

from collections import Counter

from hypothesis import given
from hypothesis import strategies as st

my_sort = sorted


@given(st.lists(st.integers()))
def test_sorting(l):
    sl = my_sort(l)

    assert isinstance(sl, list)

    assert Counter(sl) == Counter(l)

    assert all(x <= y for x, y in zip(sl, sl[1:]))

    assert my_sort(sl) == sl
