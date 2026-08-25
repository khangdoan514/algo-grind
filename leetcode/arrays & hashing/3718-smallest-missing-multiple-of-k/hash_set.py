from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen: set[int] = set(nums)
        multiple = k
        while multiple in seen:
            multiple += k

        return multiple