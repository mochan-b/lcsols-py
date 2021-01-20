from typing import List


def find_heater(house: int, heaters: List[int]) -> int:
    left = 0
    right = len(heaters) - 1
    while left <= right:
        mid = (left + right) // 2
        if heaters[mid] == house:
            return mid
        if heaters[mid] < house:
            left = mid + 1
        else:
            right = mid - 1
    return left


class Solution475:

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        radius = 0

        for house in houses:
            heater_index = find_heater(house, heaters)

            def left_dist_fn() -> int: return house - heaters[heater_index - 1]

            def right_dist_fn() -> int: return heaters[heater_index] - house

            heater_dist = right_dist_fn() if heater_index == 0 else left_dist_fn() if heater_index == len(
                heaters) else min(left_dist_fn(), right_dist_fn())

            radius = max(radius, heater_dist)

        return radius
