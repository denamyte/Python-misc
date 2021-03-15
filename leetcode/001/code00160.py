from typing import Optional, List


class ListNode:
    def __init__(self, x, nextRef=None):
        self.val = x
        self.next: Optional[ListNode] = nextRef


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/interseicton-of-two-linked-lists/
        """
        if not headA or not headB:
            return None
        end_a, count_a = self.walkToEnd(headA)
        end_b, count_b = self.walkToEnd(headB)
        if end_a is not end_b:
            return None
        min_count = min(count_a, count_b)
        headA = self.shift_head(headA, count_a, min_count)
        headB = self.shift_head(headB, count_b, min_count)
        while headA is not headB:
            headA = headA.next
            headB = headB.next
        return headA

    @staticmethod
    def walkToEnd(head: ListNode) -> (Optional[ListNode], int):
        count = 1 if head else 0
        while head and head.next:
            head = head.next
            count += 1
        return head, count

    @staticmethod
    def shift_head(head: ListNode, list_len: int, min_len: int) -> ListNode:
        while list_len > min_len:
            head = head.next
            list_len -= 1
        return head


def prepare_lists_and_call_test(a: Optional[List[int]], b: Optional[List[int]], c: Optional[List[int]]):
    head_a, tail_a = prepare_list_node(a)
    head_b, tail_b = prepare_list_node(b)
    head_c, _ = prepare_list_node(c)
    if head_c:
        tail_a.next = tail_b.next = head_c
    test(head_a, head_b, head_c)


def prepare_list_node(ar: Optional[List[int]]) -> (Optional[ListNode], Optional[ListNode]):
    """
    Create a linked list from the int list, return its head and tail nodes
    :param ar:
    :return: (head, tail)
    """
    if not ar or not len(ar):
        return None, None
    head: Optional[ListNode] = ListNode(ar[0]) if len(ar) else None
    tail: Optional[ListNode] = head
    for x in ar[1:]:
        tail.next = ListNode(x)
        tail = tail.next
    return head, tail


index = 0


def test(head_a: ListNode, head_b: ListNode, expected_node: ListNode):
    global index
    index += 1
    node = Solution().getIntersectionNode(head_a, head_b)
    print(f'''Test #{index}
----------------
connection nodes match: {expected_node == node}
''')


prepare_lists_and_call_test([4, 1],
                            [5, 6, 1],
                            [8, 4, 5])

prepare_lists_and_call_test([1, 9, 1],
                            [3],
                            [2, 4])

prepare_lists_and_call_test([2, 6, 4],
                            [1, 5],
                            None)

prepare_lists_and_call_test(None,
                            [1, 5],
                            None)

prepare_lists_and_call_test([],
                            [1, 5],
                            None)

prepare_lists_and_call_test([2, 6, 4],
                            None,
                            None)

prepare_lists_and_call_test([2, 6, 4],
                            [],
                            None)


