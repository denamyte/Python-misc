from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        https://leetcode.com/problems/linked-list-cycle/
        """
        p1 = head
        p2 = None if head is None else head.next
        while p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next
        return p2 is not None and p1 == p2


index = 0


def test(values: List[int], pos: int):
    # making a LinkedList
    head = None if not len(values) else ListNode(values[0])
    tail = head
    for val in values[1:]:
        temp = ListNode(val)
        tail.next = temp
        tail = temp
    if pos >= 0:
        point_to = head
        for _ in range(pos):
            point_to = point_to.next
        tail.next = point_to

    # testing
    global index
    index += 1
    result = Solution().hasCycle(head)
    print(f'''Test #{index}
----------------
values: {values}
   pos: {pos}
result: {result}
''')


test([], -1)
test([3, 2, 0, -4], 1)
test([1, 2], 0)
test([1], -1)
test([1], 0)
test([1, 2, 3, 4, 5, 6], -1)

