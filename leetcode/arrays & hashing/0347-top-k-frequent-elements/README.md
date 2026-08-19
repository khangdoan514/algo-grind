# 347. Top K Frequent Elements

**Medium** · [Array](https://leetcode.com/tag/array/), [Hash Table](https://leetcode.com/tag/hash-table/), [Sorting](https://leetcode.com/tag/sorting/), [Heap (Priority Queue)](https://leetcode.com/tag/heap-priority-queue/), [Bucket Sort](https://leetcode.com/tag/bucket-sort/), [Counting](https://leetcode.com/tag/counting/), [Quickselect](https://leetcode.com/tag/quickselect/), [Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/)

[Open on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/description/)

---

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

### Example 1:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

### Example 2:

```
Input: nums = [1], k = 1
Output: [1]
```

### Example 3:

```
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
```

### Constraints:

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.