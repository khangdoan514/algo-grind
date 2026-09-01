from vertical_scan import Solution

sol = Solution()

def check(strs: list[str], expected: str) -> None:
    assert sol.longestCommonPrefix(strs) == expected

def test_example_1():
    check(["flower", "flow", "flight"], "fl")

def test_example_2():
    check(["dog", "racecar", "car"], "")

def test_single_string():
    check(["hello"], "hello")

def test_all_same():
    check(["abc", "abc", "abc"], "abc")

def test_empty_prefix():
    check(["abc", "def"], "")

def test_empty_string_in_array():
    check(["", "abc"], "")