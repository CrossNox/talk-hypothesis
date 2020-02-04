from collections import Counter

from hypothesis import Verbosity, example, given, settings
from hypothesis import strategies as st


def greedy_minimum_coins(value, system):
    assert 1 in system
    system = sorted(system)

    coins_needed = []

    while value > 0:
        coin_denomination = system.pop()
        while coin_denomination <= value:
            coins_needed.append(coin_denomination)
            value -= coin_denomination
    return Counter(coins_needed)


def dynamic_minimum_coins(value, system):
    assert 1 in system
    system = sorted(system)
    count = []
    for _ in range(len(system)):
        new_list = [0 for _ in range(value + 1)]
        count.append(new_list)

    for i in range(len(system)):
        for j in range(value + 1):
            div, mod = divmod(j, system[i])
            j_prev = j - system[i]

            if i == 0:
                count[i][j] = div if mod == 0 else 0
            elif j_prev >= 0:
                min_val = min(count[i][j_prev], count[i - 1][j_prev])
                count[i][j] = min_val + 1
            else:
                count[i][j] = count[i - 1][j]

    coins = []
    remaining_coins, coin_idx = min(
        (l[value - sum(coins)], idx) for idx, l in enumerate(count)
    )

    while sum(coins) != value:
        coins.append(system[coin_idx])
        remaining_coins, coin_idx = min(
            (l[value - sum(coins)], idx) for idx, l in enumerate(count)
        )

    return Counter(coins)


@st.composite
def coin_systems(draw):
    cs = draw(st.lists(st.integers(min_value=2, max_value=10), unique=True, min_size=0))
    cs.append(1)
    return cs


# @example(9, [1,3,6])
# @example(15, [1, 7, 10])
# @settings(verbosity=Verbosity.debug)
@given(st.integers(max_value=100, min_value=1), coin_systems())
def test_change(value, system):
    assert sum(greedy_minimum_coins(value, system).values()) == sum(
        dynamic_minimum_coins(value, system).values()
    )
