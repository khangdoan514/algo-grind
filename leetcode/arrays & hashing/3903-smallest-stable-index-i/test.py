from prefix_suffix import Solution

sol = Solution()

def check(nums: list[int], k: int, expected: int) -> None:
    assert sol.firstStableIndex(nums, k) == expected

def test_example_1():
    check([5, 0, 1, 4], 3, 3)

def test_example_2():
    check([3, 2, 1], 1, -1)

def test_example_3():
    check([0], 0, 0)

def test_stable_at_start():
    check([1, 2, 3], 2, 0)

def test_all_equal():
    check([4, 4, 4], 0, 0)
