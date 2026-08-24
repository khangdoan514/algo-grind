from kadane import Solution as Kadane
from divide_and_conquer import Solution as DivideAndConquer

solutions = [Kadane(), DivideAndConquer()]

def check(nums: list[int], expected: int) -> None:
    for sol in solutions:
        assert sol.maxSubArray(nums) == expected

def test_example_1():
    check([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)

def test_example_2():
    check([1], 1)

def test_example_3():
    check([5, 4, -1, 7, 8], 23)

def test_all_negative():
    check([-3, -2, -5], -2)

def test_single_negative():
    check([-1], -1)