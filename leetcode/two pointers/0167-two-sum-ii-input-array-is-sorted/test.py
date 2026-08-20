from two_pointers import Solution

sol = Solution()

def check(numbers: list[int], target: int, expected: list[int]) -> None:
    result = sol.twoSum(numbers, target)
    assert result == expected
    assert numbers[result[0] - 1] + numbers[result[1] - 1] == target

def test_example_1():
    check([2, 7, 11, 15], 9, [1, 2])

def test_example_2():
    check([2, 3, 4], 6, [1, 3])

def test_example_3():
    check([-1, 0], -1, [1, 2])

def test_same_values():
    check([1, 2, 3, 4, 4, 9], 8, [4, 5])

def test_negatives():
    check([-5, -3, -1, 0, 2], -4, [2, 3])