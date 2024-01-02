import pytest
import Function


@pytest.mark.chaya
def test_find_primes():
    assert Function.find_primes(8) == {1, 2, 3, 5, 7}
    assert Function.find_primes(18) == {1, 2, 3, 5, 7, 11, 13, 17}
    assert Function.find_primes(10) == {1, 2, 3, 5, 7}


@pytest.mark.parametrize("mylist , res", [([7, 8, 1, 0, 5], [0, 1, 5, 7, 8]), ([9, 7, 8], [7, 8, 9])])
def test_sort_list(mylist, res):
    assert Function.sort_list(mylist) == res
