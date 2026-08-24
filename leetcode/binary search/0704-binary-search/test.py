from binary_search import Solution

sol = Solution()

def check(nums: list[int], target: int, expected: int) -> None:
    assert sol.search(nums, target) == expected

def test_example_1():
    check([-1, 0, 3, 5, 9, 12], 9, 4)

def test_example_2():
    check([-1, 0, 3, 5, 9, 12], 2, -1)

def test_single_found():
    check([5], 5, 0)

def test_single_missing():
    check([5], -5, -1)

def test_first_element():
    check([-1, 0, 3, 5, 9, 12], -1, 0)

def test_last_element():
    check([-1, 0, 3, 5, 9, 12], 12, 5)