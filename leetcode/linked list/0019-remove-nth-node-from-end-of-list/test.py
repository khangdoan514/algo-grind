from list_node import ListNode
from two_pointers import Solution

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

def check(values: list[int], n: int, expected: list[int]) -> None:
    result = sol.removeNthFromEnd(from_list(values), n)
    assert to_list(result) == expected

def test_example_1():
    check([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])

def test_example_2():
    check([1], 1, [])

def test_example_3():
    check([1, 2], 1, [1])

def test_remove_head():
    check([1, 2], 2, [2])

def test_remove_last():
    check([1, 2, 3], 1, [1, 2])
