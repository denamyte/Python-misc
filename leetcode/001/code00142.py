from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pass
