from binary_search import Solution

sol = Solution()

def check(arr: list[int], expected: int) -> None:
    assert sol.peakIndexInMountainArray(arr) == expected

def test_example_1():
    check([0, 1, 0], 1)

def test_example_2():
    check([0, 2, 1, 0], 1)

def test_example_3():
    check([0, 10, 5, 2], 1)

def test_peak_near_end():
    check([1, 2, 3, 4, 1], 3)

def test_peak_near_start():
    check([1, 5, 4, 3, 2], 1)