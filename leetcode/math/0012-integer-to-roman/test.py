from greedy import Solution

sol = Solution()

def check(num: int, expected: str) -> None:
    assert sol.intToRoman(num) == expected

def test_example_1():
    check(3749, "MMMDCCXLIX")

def test_example_2():
    check(58, "LVIII")

def test_example_3():
    check(1994, "MCMXCIV")

def test_single_digit():
    check(3, "III")

def test_subtractive_four():
    check(4, "IV")

def test_subtractive_nine():
    check(9, "IX")

def test_minimum():
    check(1, "I")

def test_maximum():
    check(3999, "MMMCMXCIX")