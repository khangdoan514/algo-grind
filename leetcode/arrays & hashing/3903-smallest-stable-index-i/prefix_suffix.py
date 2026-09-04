from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = [0] * n
        right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        left = 0
        for i, num in enumerate(nums):
            left = max(left, num)
            if left - right[i] <= k:
                return i

        return -1
