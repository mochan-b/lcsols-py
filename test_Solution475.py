from Solution475 import Solution475
import pytest


def test_solution475_1():
    houses = [1, 2, 3]
    heaters = [2]
    solution = Solution475()
    assert solution.findRadius(houses, heaters) == 1


def test_solution475_2():
    houses = [1, 3, 2]
    heaters = [2]
    solution = Solution475()
    assert solution.findRadius(houses, heaters) == 1


def test_solution475_3():
    houses = [1, 2, 3, 4]
    heaters = [1, 4]
    solution = Solution475()
    assert solution.findRadius(houses, heaters) == 1


def test_solution475_4():
    houses = [1, 5]
    heaters = [2]
    solution = Solution475()
    assert solution.findRadius(houses, heaters) == 3


def test_solution475_5():
    houses = [1, 5]
    heaters = [10]
    solution = Solution475()
    assert solution.findRadius(houses, heaters) == 9


def test_solution475_6():
    houses = [282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923]
    heaters = [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840,
               143542612]
    solution = Solution475()
    assert solution.findRadius(houses, heaters) == 161834419


def test_solution475_6():
    houses = [474833169, 264817709, 998097157, 817129560]
    heaters = [197493099, 404280278, 893351816, 505795335]
    solution = Solution475()
    assert solution.findRadius(houses, heaters) == 104745341
