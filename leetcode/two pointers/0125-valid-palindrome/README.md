# 125. Valid Palindrome

**Easy** · [Two Pointers](https://leetcode.com/tag/two-pointers/), [String](https://leetcode.com/tag/string/)

**Companies:** [Yandex](https://leetcode.com/company/yandex/?favoriteSlug=yandex-thirty-days), [BCG](https://leetcode.com/company/bcg/?favoriteSlug=bcg-thirty-days), [CleverTap](https://leetcode.com/company/clevertap/?favoriteSlug=clevertap-thirty-days), [Google](https://leetcode.com/company/google/?favoriteSlug=google-thirty-days), [Microsoft](https://leetcode.com/company/microsoft/?favoriteSlug=microsoft-thirty-days), [TCS](https://leetcode.com/company/tcs/?favoriteSlug=tcs-thirty-days), [Amazon](https://leetcode.com/company/amazon/?favoriteSlug=amazon-thirty-days), [Bloomberg](https://leetcode.com/company/bloomberg/?favoriteSlug=bloomberg-thirty-days), [Oracle](https://leetcode.com/company/oracle/?favoriteSlug=oracle-thirty-days), [Meta](https://leetcode.com/company/facebook/?favoriteSlug=facebook-thirty-days), [Cisco](https://leetcode.com/company/cisco/?favoriteSlug=cisco-thirty-days), [Comcast](https://leetcode.com/company/comcast/?favoriteSlug=comcast-thirty-days), [Tiktok](https://leetcode.com/company/tiktok/?favoriteSlug=tiktok-thirty-days), [Uber](https://leetcode.com/company/uber/?favoriteSlug=uber-thirty-days), [Zoho](https://leetcode.com/company/zoho/?favoriteSlug=zoho-thirty-days), [Axon](https://leetcode.com/company/axon/?favoriteSlug=axon-thirty-days), [Deloitte](https://leetcode.com/company/deloitte/?favoriteSlug=deloitte-thirty-days), [HCL](https://leetcode.com/company/hcl/?favoriteSlug=hcl-thirty-days), [Infosys](https://leetcode.com/company/infosys/?favoriteSlug=infosys-thirty-days)

[Open on LeetCode](https://leetcode.com/problems/valid-palindrome/description/)

---

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if `s` is a **palindrome**, or `false` otherwise.

### Example 1:

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### Example 2:

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Example 3:

```
Input: s = " "
Output: true
Explanation: s is an empty string after removing non-alphanumeric characters.
```

### Constraints:

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.