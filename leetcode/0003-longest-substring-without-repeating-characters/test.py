from sliding_window import Solution

sol = Solution()

def check(s: str, expected: int) -> None:
    assert sol.lengthOfLongestSubstring(s) == expected

def test_example_1():
    check("abcabcbb", 3)

def test_example_2():
    check("bbbbb", 1)

def test_example_3():
    check("pwwkew", 3)

def test_empty():
    check("", 0)

def test_single_char():
    check("a", 1)

def test_all_unique():
    check("abcdef", 6)

def test_spaces_and_symbols():
    check("a b!a", 4)