# 20. Valid Parentheses

**Easy** · [String](https://leetcode.com/tag/string/), [Stack](https://leetcode.com/tag/stack/)

**Companies:** [Apple](https://leetcode.com/company/apple/?favoriteSlug=apple-thirty-days), [Zoho](https://leetcode.com/company/zoho/?favoriteSlug=zoho-thirty-days), [Google](https://leetcode.com/company/google/?favoriteSlug=google-thirty-days), [Walmart Labs](https://leetcode.com/company/walmart-labs/?favoriteSlug=walmart-labs-thirty-days), [Tiktok](https://leetcode.com/company/tiktok/?favoriteSlug=tiktok-thirty-days), [Yandex](https://leetcode.com/company/yandex/?favoriteSlug=yandex-thirty-days), [Meta](https://leetcode.com/company/facebook/?favoriteSlug=facebook-thirty-days), [Turing](https://leetcode.com/company/turing/?favoriteSlug=turing-thirty-days), [Zulily](https://leetcode.com/company/zulily/?favoriteSlug=zulily-thirty-days), [Cerner](https://leetcode.com/company/cerner/?favoriteSlug=cerner-thirty-days), [LinkedIn](https://leetcode.com/company/linkedin/?favoriteSlug=linkedin-thirty-days), [EPAM Systems](https://leetcode.com/company/epam-systems/?favoriteSlug=epam-systems-thirty-days), [Udemy](https://leetcode.com/company/udemy/?favoriteSlug=udemy-thirty-days), [Amazon](https://leetcode.com/company/amazon/?favoriteSlug=amazon-thirty-days), [Bloomberg](https://leetcode.com/company/bloomberg/?favoriteSlug=bloomberg-thirty-days), [TripAdvisor](https://leetcode.com/company/tripadvisor/?favoriteSlug=tripadvisor-thirty-days), [IBM](https://leetcode.com/company/ibm/?favoriteSlug=ibm-thirty-days), [Intuit](https://leetcode.com/company/intuit/?favoriteSlug=intuit-thirty-days), [Microsoft](https://leetcode.com/company/microsoft/?favoriteSlug=microsoft-thirty-days), [Oracle](https://leetcode.com/company/oracle/?favoriteSlug=oracle-thirty-days), [Autodesk](https://leetcode.com/company/autodesk/?favoriteSlug=autodesk-thirty-days), [Epic Systems](https://leetcode.com/company/epic-systems/?favoriteSlug=epic-systems-thirty-days), [Infosys](https://leetcode.com/company/infosys/?favoriteSlug=infosys-thirty-days), [NVIDIA](https://leetcode.com/company/nvidia/?favoriteSlug=nvidia-thirty-days), [Odoo](https://leetcode.com/company/odoo/?favoriteSlug=odoo-thirty-days), [Qualcomm](https://leetcode.com/company/qualcomm/?favoriteSlug=qualcomm-thirty-days), [Sony](https://leetcode.com/company/sony/?favoriteSlug=sony-thirty-days), [TCS](https://leetcode.com/company/tcs/?favoriteSlug=tcs-thirty-days), [Two Sigma](https://leetcode.com/company/two-sigma/?favoriteSlug=two-sigma-thirty-days)

[Open on LeetCode](https://leetcode.com/problems/valid-parentheses/description/)

---

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Example 1:

```
Input: s = "()"
Output: true
```

### Example 2:

```
Input: s = "()[]{}"
Output: true
```

### Example 3:

```
Input: s = "(]"
Output: false
```

### Example 4:

```
Input: s = "([])"
Output: true
```

### Example 5:

```
Input: s = "([)]"
Output: false
```

### Constraints:

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.