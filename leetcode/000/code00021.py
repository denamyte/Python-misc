from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge Two Sorted Lists: https://leetcode.com/problems/merge-two-sorted-lists/"""
        h1, h2, h3 = ListNode(0, l1), ListNode(0, l2), ListNode(0)
        h3_tail = h3
        while h1.next and h2.next:
            head = h1 if h1.next.val <= h2.next.val else h2
            node = head.next
            head.next = head.next.next
            node.next = None
            h3_tail.next = node
            h3_tail = h3_tail.next

        h3_tail.next = h1.next if h1.next else (h2.next if h2.next else None)
        return h3.next


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


def test(l1: List[int], l2: List[int], expected_merged: List[int]):
    global index
    index += 1
    result_node = Solution().mergeTwoLists(ar_to_node(l1), ar_to_node(l2))
    result = node_to_ar(result_node)
    print(f'''\
Test #{index}
----------------------------------------------------
                 List 1: {l1}
                 List 2: {l2}
                 Result: {result}
Result matches expected: {result == expected_merged}
''')


test([1, 2, 4],
     [1, 3, 4],
     [1, 1, 2, 3, 4, 4])

test([], [], [])

test([], [1], [1])

test([1], [], [1])

test([-2, 2, 3, 10, 12, 20],
     [-4, -2, -2, 0, 3, 9, 10, 10],
     [-4, -2, -2, -2, 0, 2, 3, 3, 9, 10, 10, 10, 12, 20])
