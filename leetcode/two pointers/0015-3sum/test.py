from two_pointers import Solution

sol = Solution()

def check(nums: list[int], expected: list[list[int]]) -> None:
    result = sol.threeSum(nums)
    assert sorted(sorted(triplet) for triplet in result) == sorted(sorted(triplet) for triplet in expected)

def test_example_1():
    check([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])

def test_example_2():
    check([0, 1, 1], [])

def test_example_3():
    check([0, 0, 0], [[0, 0, 0]])

def test_no_triplets():
    check([1, 2, 3], [])

def test_multiple_zeros():
    check([0, 0, 0, 0], [[0, 0, 0]])
