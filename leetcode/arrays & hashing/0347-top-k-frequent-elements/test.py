from bucket_sort import Solution

sol = Solution()

def check(nums: list[int], k: int, expected: list[int]) -> None:
    assert sorted(sol.topKFrequent(nums, k)) == sorted(expected)

def test_example_1():
    check([1, 1, 1, 2, 2, 3], 2, [1, 2])

def test_example_2():
    check([1], 1, [1])

def test_example_3():
    check([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2])

def test_k_equals_all():
    check([1, 2, 3], 3, [1, 2, 3])

def test_negatives():
    check([-1, -1, -1, 2, 2, 3], 2, [-1, 2])