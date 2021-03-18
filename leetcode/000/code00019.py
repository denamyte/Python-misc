from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        """
        p1, p2 = head, head,
        step = 0
        while p1:
            p1 = p1.next
            step += 1
            if step - 1 > n:
                p2 = p2.next
        if step - n == 0:
            return head.next
        p2.next = p2.next.next
        return head


index = 0


def test(ar: List[int], n: int, exp_result: List[int]):
    global index
    index += 1
    head = ar_to_node(ar)
    result = Solution().removeNthFromEnd(head, n)
    print(f'''Test #{index}
----------------
  List to process: {ar};
  Remove from end: {n};
  Expected result: {exp_result};
Result is correct: {node_to_ar(result) == exp_result}
''')


def ar_to_node(ar: List[int]):
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


# [1, 2, 3, 4, 5] ======================
test([1, 2, 3, 4, 5],
     1,
     [1, 2, 3, 4])

test([1, 2, 3, 4, 5],
     2,
     [1, 2, 3, 5])

test([1, 2, 3, 4, 5],
     3,
     [1, 2, 4, 5])

test([1, 2, 3, 4, 5],
     4,
     [1, 3, 4, 5])

test([1, 2, 3, 4, 5],
     5,
     [2, 3, 4, 5])

# [1, 2, 3] =====================
test([1, 2, 3],
     1,
     [1, 2])

test([1, 2, 3],
     2,
     [1, 3])

test([1, 2, 3],
     3,
     [2, 3])

#[1, 2]
test([1, 2],
     1,
     [1])

test([1, 2],
     2,
     [2])

# [1]
test([1],
     1,
     [])


