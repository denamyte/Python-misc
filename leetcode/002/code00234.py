from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        count = self.length(head)
        if count < 2:
            return True
        middle = count // 2
        rev_node = self.reverse(self.walk(head, middle + count % 2))
        return self.coincide(head, rev_node, middle)

    def length(self, node: ListNode) -> int:
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def walk(self, node: ListNode, steps: int) -> ListNode:
        while node and steps:
            node = node.next
            steps -= 1
        return node

    def reverse(self, node: ListNode) -> ListNode:
        tail = node
        head = node
        while tail.next:
            curr = tail.next
            tail.next = tail.next.next
            curr.next = head
            head = curr
        return head

    def coincide(self, h1: ListNode, h2: ListNode, steps: int) -> bool:
        while steps and h1.val == h2.val:
            steps -= 1
            h1, h2 = h1.next, h2.next
        return steps == 0


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


def test(head_ar: List[int], expected_is_pal: bool):
    global index
    index += 1
    result_is_pal = Solution().isPalindrome(ar_to_node(head_ar))
    print(f'''Test #{index}
------------------
          original list: {head_ar}
 result 'is palindrome': {'Yes' if result_is_pal else 'No'}
result matches expected: {result_is_pal == expected_is_pal} 
''')


test([], True)
test([1], True)
test([1, 2], False)
test([1, 2, 1], True)
test([1, 2, 2, 3], False)
test([1, 2, 2, 1], True)
test([1, 2, 3, 0, 1], False)
test([1, 5, 3, 5, 1], True)
