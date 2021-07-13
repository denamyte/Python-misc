class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next: Node = next
        self.random: Node = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        curr = head
        while curr:  # Interweaving with new nodes
            node = Node(curr.val, curr.next, curr.random)
            curr.next = node
            curr = curr.next.next

        old = head
        head = head.next
        while old:
            node = old.next
            old = node.next

            if old:
                node.next = old.next
            if node.random:
                node.random = node.random.next

        return head
