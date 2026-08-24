from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            left_best = solve(left, mid)
            right_best = solve(mid + 1, right)

            cross_left = nums[mid]
            total = 0
            for i in range(mid, left - 1, -1):
                total += nums[i]
                cross_left = max(cross_left, total)

            cross_right = nums[mid + 1]
            total = 0
            for i in range(mid + 1, right + 1):
                total += nums[i]
                cross_right = max(cross_right, total)

            return max(left_best, right_best, cross_left + cross_right)

        return solve(0, len(nums) - 1)