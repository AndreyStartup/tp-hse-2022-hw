import random
import pytest
import Functions
import time


@pytest.mark.parametrize("array,expected", [([0, 3, -4, -5, -6], -12),
                                            ([100023, 36247, 5555, -3249], 138576),
                                            ([12346, 695, -123, 38743], 51661),
                                            ([85123, -543680, 272, 12],  -458273)])
def test_sum(array, expected):
    assert Functions._sum(array) == 1

@pytest.mark.parametrize("array,expected", [([0, 3, -4, -5, -6], 0),
                                            ([100023, 36247, 5555, -3249], -65434338853755795),
                                            ([12346, 695, -123, -38743], 40889277352830),
                                            ([85123, -543680, 272, 12],  -151056851496960)])
def test_mult(array, expected):
    assert Functions._mult(array) == expected

@pytest.mark.parametrize("array,expected", [([0, 3, -4, -5, -6, -6, 3], 3),
                                            ([100023, 36247, 5555, -3249], 100023),
                                            ([12346, 695, -123, -38743], 12346),
                                            ([85123, -543680, 272, 12],  85123)])
def test_max(array, expected):
    assert Functions._max(array) == expected

@pytest.mark.parametrize("array,expected", [([0, 3, -4, -5, -6, -6], -6),
                                            ([100023, 36247, 5555, -3249], -3249),
                                            ([12346, 695, -123, -38743], -38743),
                                            ([85123, -543680, 272, 12],  -543680)])
def test_min(array, expected):
    assert Functions._min(array) == expected


def test_read_from_file():
    with open('test_file.txt', mode='w+') as fp:
        for i in range(1, 10):
            fp.write(f'{i} ')
        fp.seek(0)
        fp.read()
        fp.close()

    assert Functions.read_from_file('test_file.txt') == [1, 2, 3, 4, 5, 6, 7, 8, 9]