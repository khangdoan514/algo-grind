from hash_set import Solution

sol = Solution()

def check(nums: list[int], expected: bool) -> None:
    assert sol.containsDuplicate(nums) == expected

def test_example_1():
    check([1, 2, 3, 1], True)

def test_example_2():
    check([1, 2, 3, 4], False)

def test_example_3():
    check([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)

def test_single():
    check([1], False)

def test_negatives():
    check([-1, -2, -1], True)

def test_two_same():
    check([7, 7], True)