import time

import pytest

from source.my_functions import add, divide


def test_add():
    assert add(1, 5) == 6


def test_divide():
    assert divide(10, 2) == 5


def test_add_strings():
    assert add('I like ', 'burgers') == 'I like burgers'


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    assert add(2, 2) == 4


@pytest.mark.skip(reason='this feature is currently broken')
def test_add():
    assert add(1, 2) == 3


@pytest.mark.xfail(reason='we know we cannot divide by zero')
def test_divide_zero_broken():
    divide(4, 0)
