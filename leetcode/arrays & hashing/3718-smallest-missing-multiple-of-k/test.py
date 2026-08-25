from hash_set import Solution

sol = Solution()

def check(nums: list[int], k: int, expected: int) -> None:
    assert sol.missingMultiple(nums, k) == expected

def test_example_1():
    check([8, 2, 3, 4, 6], 2, 10)

def test_example_2():
    check([1, 4, 7, 10, 15], 5, 5)

def test_k_missing_from_start():
    check([3, 6, 9], 3, 12)

def test_all_multiples_present():
    check([2, 4, 6, 8], 2, 10)

def test_single_element():
    check([7], 7, 14)