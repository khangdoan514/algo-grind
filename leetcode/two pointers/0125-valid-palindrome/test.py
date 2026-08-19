from two_pointers import Solution

sol = Solution()

def check(s: str, expected: bool) -> None:
    assert sol.isPalindrome(s) == expected

def test_example_1():
    check("A man, a plan, a canal: Panama", True)

def test_example_2():
    check("race a car", False)

def test_example_3():
    check(" ", True)

def test_only_punctuation():
    check(".,;!? ", True)

def test_case_insensitive():
    check("No 'x' in Nixon", True)