from hash_map import Solution

sol = Solution()

def check(strs: list[str], expected: list[list[str]]) -> None:
    result = sol.groupAnagrams(strs)
    assert sorted(sorted(group) for group in result) == sorted(sorted(group) for group in expected)

def test_example_1():
    check(["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

def test_example_2():
    check([""], [[""]])

def test_example_3():
    check(["a"], [["a"]])

def test_no_anagrams():
    check(["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]])

def test_all_same_anagram_group():
    check(["ab", "ba"], [["ab", "ba"]])