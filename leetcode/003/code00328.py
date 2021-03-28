from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd_head = head.next
        tails = [head, odd_head]  # even and odd tails
        count = 1
        while tails[count & 1].next:
            # updating current "crop node"
            node = tails[count & 1].next
            tails[count & 1].next = None

            count += 1
            # updating current "grow node"
            tails[count & 1].next = node
            tails[count & 1] = tails[count & 1].next

        # connecting both parts
        tails[0].next = odd_head
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


def test(head_ar: List[int], expected_ar: List[int]):
    global index
    index += 1
    result_node = Solution().oddEvenList(ar_to_node(head_ar))
    result_ar = node_to_ar(result_node)
    print(f'''Test #{index}
------------------
          original list: {head_ar}
            result list: {result_ar}
result matches expected: {expected_ar == result_ar} 
''')


test([1, 2, 3, 4, 5],
     [1, 3, 5, 2, 4])
test([2, 1, 3, 5, 6, 4, 7],
     [2, 3, 6, 7, 1, 5, 4])
test([],
     [])
test([1],
     [1])
test([1, 2],
     [1, 2])
test([1, 2, 3],
     [1, 3, 2])
test([1, 2, 3, 4],
     [1, 3, 2, 4])
test([1, 2, 3, 4],
     [1, 3, 2, 4])
