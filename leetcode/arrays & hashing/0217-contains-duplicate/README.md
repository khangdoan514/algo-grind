# 217. Contains Duplicate

**Easy** · [Array](https://leetcode.com/tag/array/), [Hash Table](https://leetcode.com/tag/hash-table/), [Sorting](https://leetcode.com/tag/sorting/)

**Companies:** [TCS](https://leetcode.com/company/tcs/?favoriteSlug=tcs-thirty-days), [Google](https://leetcode.com/company/google/?favoriteSlug=google-thirty-days), [Amazon](https://leetcode.com/company/amazon/?favoriteSlug=amazon-thirty-days), [Accenture](https://leetcode.com/company/accenture/?favoriteSlug=accenture-thirty-days), [IBM](https://leetcode.com/company/ibm/?favoriteSlug=ibm-thirty-days), [Meta](https://leetcode.com/company/facebook/?favoriteSlug=facebook-thirty-days), [Netflix](https://leetcode.com/company/netflix/?favoriteSlug=netflix-thirty-days), [Apple](https://leetcode.com/company/apple/?favoriteSlug=apple-thirty-days), [Capgemini](https://leetcode.com/company/capgemini/?favoriteSlug=capgemini-thirty-days), [Microsoft](https://leetcode.com/company/microsoft/?favoriteSlug=microsoft-thirty-days), [Oracle](https://leetcode.com/company/oracle/?favoriteSlug=oracle-thirty-days), [Yahoo](https://leetcode.com/company/yahoo/?favoriteSlug=yahoo-thirty-days), [Zoho](https://leetcode.com/company/zoho/?favoriteSlug=zoho-thirty-days), [Bloomberg](https://leetcode.com/company/bloomberg/?favoriteSlug=bloomberg-thirty-days), [Infosys](https://leetcode.com/company/infosys/?favoriteSlug=infosys-thirty-days)

[Open on LeetCode](https://leetcode.com/problems/contains-duplicate/description/)

---

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### Example 1:

```
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.
```

### Example 2:

```
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.
```

### Example 3:

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

### Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`