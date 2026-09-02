from dynamic_programming import Solution

sol = Solution()

def check(s: str, p: str, expected: bool) -> None:
    assert sol.isMatch(s, p) == expected

def test_example_1():
    check("aa", "a", False)

def test_example_2():
    check("aa", "a*", True)

def test_example_3():
    check("ab", ".*", True)

def test_star_zero_matches():
    check("aab", "c*a*b", True)

def test_no_match():
    check("mississippi", "mis*is*p*.", False)

def test_dot_match():
    check("abc", "a.c", True)
