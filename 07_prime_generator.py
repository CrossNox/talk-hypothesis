import math

from hypothesis import Verbosity as h_Verbosity
from hypothesis import given
from hypothesis import settings as h_settings
from hypothesis import strategies as st


def generate_prime(seed):
    prime = seed ** 2 + seed + 41
    print(f"{seed} ==> {prime}")
    return prime


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


@h_settings(verbosity=h_Verbosity.verbose)
@given(st.integers(min_value=1))
def test_all_primes(seed):
    assert is_prime(generate_prime(seed))
