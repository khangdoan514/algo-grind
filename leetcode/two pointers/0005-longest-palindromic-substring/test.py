from expand_around_center import Solution

sol = Solution()

def check(s: str, expected: str | list[str]) -> None:
    result = sol.longestPalindrome(s)
    if isinstance(expected, list):
        assert result in expected
    else:
        assert result == expected

def test_example_1():
    check("babad", ["bab", "aba"])

def test_example_2():
    check("cbbd", "bb")

def test_single_char():
    check("a", "a")

def test_all_same():
    check("aaa", "aaa")

def test_even_palindrome():
    check("abba", "abba")