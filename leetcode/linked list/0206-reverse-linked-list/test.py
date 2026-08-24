from list_node import ListNode
from iterative import Solution

sol = Solution()

def to_list(head: ListNode | None) -> list[int]:
    values: list[int] = []
    while head:
        values.append(head.val)
        head = head.next

    return values

def from_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    curr = dummy
    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next

def check(values: list[int], expected: list[int]) -> None:
    result = sol.reverseList(from_list(values))
    assert to_list(result) == expected

def test_example_1():
    check([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

def test_example_2():
    check([1, 2], [2, 1])

def test_example_3():
    check([], [])

def test_single():
    check([1], [1])