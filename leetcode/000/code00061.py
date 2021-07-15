# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not k or not head or not head.next:  # after this: k > 0, length > 1
            return head

        last, length = self.findLastAndLength(head)

        k %= length
        if not k:
            return head

        last.next = head

        for _ in range(length - k):
            last = last.next

        head = last.next
        last.next = None

        return head

    @staticmethod
    def findLastAndLength(node: ListNode) -> (ListNode, int):
        last, length = node, 0
        while node:
            last = node
            length += 1
            node = node.next
        return last, length


def ar_to_node(ar: List[int]):
    if not len(ar):
        return None
    head = ListNode(ar[-1])
    for x in ar[-2::-1]:
        head = ListNode(x, head)
    return head


def node_to_ar(head: ListNode):
    ar = []
    while head:
        ar.append(head.val)
        head = head.next
    return ar


index = 0


def test(l1: List[int], k, expected: List[int]):
    global index
    index += 1
    head = ar_to_node(l1)

    result_node = Solution().rotateRight(head, k)
    result = node_to_ar(result_node)
    print(f'''\
Test #{index}
----------------------------------------------------
               List arg: {l1}
               Rotate k: {k}
               List res: {result}
Result matches expected: {result == expected}
''')


test([1, 2, 3, 4, 5],
     0,
     [1, 2, 3, 4, 5])

test([1, 2, 3, 4, 5],
     1,
     [5, 1, 2, 3, 4])

test([1, 2, 3, 4, 5],
     2,
     [4, 5, 1, 2, 3])

test([1, 2, 3, 4, 5],
     3,
     [3, 4, 5, 1, 2])

test([1, 2, 3, 4, 5],
     4,
     [2, 3, 4, 5, 1])

test([1, 2, 3, 4, 5],
     5,
     [1, 2, 3, 4, 5])

test([1, 2, 3, 4, 5],
     6,
     [5, 1, 2, 3, 4])

test([],
     1,
     [])

test([1],
     0,
     [1])

test([1],
     1,
     [1])

test([1, 2],
     1,
     [2, 1])
