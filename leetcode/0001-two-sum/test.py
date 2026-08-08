from hash_map import Solution

sol = Solution()

def check(nums: list[int], target: int, expected: list[int]) -> None:
    result = sol.twoSum(nums, target)
    assert sorted(result) == sorted(expected)
    assert nums[result[0]] + nums[result[1]] == target
    assert result[0] != result[1]

def test_example_1():
    check([2, 7, 11, 15], 9, [0, 1])

def test_example_2():
    check([3, 2, 4], 6, [1, 2])

def test_example_3():
    check([3, 3], 6, [0, 1])

def test_negatives():
    check([-1, -2, -3, -4, -5], -8, [2, 4])

def test_mixed_signs():
    check([-3, 4, 3, 90], 0, [0, 2])

def test_target_at_ends():
    check([1, 5, 3, 7, 2], 3, [0, 4])