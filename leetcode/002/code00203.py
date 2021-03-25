from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        cursor = head
        while cursor and cursor.next:
            if cursor.next.val != val:
                cursor = cursor.next
            else:
                cursor.next = cursor.next.next
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


def test(head_ar: List[int], val: int, expected_result: List[int]):
    global index
    index += 1
    result_node = Solution().removeElements(ar_to_node(head_ar), val)
    result_ar = node_to_ar(result_node)
    print(f'''Test #{index}
------------------
          original list: {head_ar}
            remove item: {val}
            result list: {result_ar}
result matches expected: {expected_result == result_ar} 
''')


test([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5])
test([], 1, [])
test([7, 7, 7, 7], 7, [])
test([7, 7, 7, 7, 7, 1, 7, 7, 7, 2, 7, 7, 7], 7, [1, 2])
