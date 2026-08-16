from dummy_node import ListNode, Solution

sol = Solution()

def to_list(head: ListNode | None) -> list[int]:
    values: list[int] = []
    while head:
        values.append(head.val)
        head = head.next
    return values

def from_list(values: list[int]) -> ListNode:
    dummy = ListNode()
    curr = dummy
    for value in values:
        curr.next = ListNode(value)
        curr = curr.next
    return dummy.next

def check(l1: list[int], l2: list[int], expected: list[int]) -> None:
    result = sol.addTwoNumbers(from_list(l1), from_list(l2))
    assert to_list(result) == expected

def test_example_1():
    check([2, 4, 3], [5, 6, 4], [7, 0, 8])

def test_example_2():
    check([0], [0], [0])

def test_example_3():
    check([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])

def test_unequal_lengths():
    check([1, 8], [0], [1, 8])

def test_carry_creates_extra_digit():
    check([5], [5], [0, 1])

def test_long_carry_chain():
    check([9, 9, 9], [1], [0, 0, 0, 1])