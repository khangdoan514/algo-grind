from stack import Solution

sol = Solution()

def check(s: str, expected: bool) -> None:
    assert sol.isValid(s) == expected

def test_example_1():
    check("()", True)

def test_example_2():
    check("()[]{}", True)

def test_example_3():
    check("(]", False)

def test_example_4():
    check("([])", True)

def test_example_5():
    check("([)]", False)

def test_single_open():
    check("(", False)

def test_empty_close_first():
    check(")", False)