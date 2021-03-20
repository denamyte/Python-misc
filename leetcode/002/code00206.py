from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return Solution.reverse_recursively(head)[0]
        # return Solution.reverse_iteratively(head)

    @staticmethod
    def reverse_recursively(head: ListNode) -> (ListNode, ListNode):
        if head and head.next:
            new_head, tail = Solution.reverse_recursively(head.next)
            tail.next = head
            head.next = None
            return new_head, head
        return head, head

    @staticmethod
    def reverse_iteratively(head: ListNode) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head
        while tail.next:
            new_head = tail.next
            tail.next = new_head.next
            new_head.next = head
            head = new_head
        return head


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


def test(head_ar: List[int], expected_reversed: List[int]):
    global index
    index += 1
    head = ar_to_node(head_ar)
    reversed_head = Solution().reverseList(head)
    reversed_ar = node_to_ar(reversed_head)
    print(f'''Test #{index}
------------------
   original list: {head_ar}
   reversed list: {reversed_ar}
expected matches: {expected_reversed == reversed_ar} 
''')


test([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

test([1, 2], [2, 1])

test([1], [1])

test([], [])
