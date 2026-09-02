from sliding_window import Solution

sol = Solution()

def check(haystack: str, needle: str, expected: int) -> None:
    assert sol.strStr(haystack, needle) == expected

def test_example_1():
    check("sadbutsad", "sad", 0)

def test_example_2():
    check("leetcode", "leeto", -1)

def test_needle_at_end():
    check("hello", "lo", 3)

def test_needle_equals_haystack():
    check("abc", "abc", 0)

def test_needle_longer_than_haystack():
    check("ab", "abc", -1)

def test_second_occurrence_not_returned():
    check("sadbutsad", "but", 3)
