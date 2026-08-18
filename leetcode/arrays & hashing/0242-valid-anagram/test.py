from hash_map import Solution

sol = Solution()

def check(s: str, t: str, expected: bool) -> None:
    assert sol.isAnagram(s, t) == expected

def test_example_1():
    check("anagram", "nagaram", True)

def test_example_2():
    check("rat", "car", False)

def test_different_lengths():
    check("ab", "abc", False)

def test_same_string():
    check("abc", "abc", True)

def test_repeated_chars():
    check("aab", "aba", True)

def test_same_length_not_anagram():
    check("aab", "abb", False)