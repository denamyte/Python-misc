from typing import Optional, List


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val: int = val
        self.prev: Node = prev
        self.next: Node = next
        self.child: Node = child


class Solution:
    def flatten(self, head: Node) -> Node:
        temp_head = Node(0, None, None, None)
        self.add_node(temp_head, head)
        if temp_head.next:
            temp_head.next.prev = None
        return temp_head.next

    def add_node(self, tail: Node, curr: Node) -> Node:
        if curr is None:
            return tail
        node, child, nxt = self.disassemble(curr)
        tail.next = node
        node.prev = tail

        tail = self.add_node(node, child)
        return self.add_node(tail, nxt)

    @staticmethod
    def disassemble(node: Node) -> (Node, Optional[Node], Optional[Node],):
        child_node, next_node = node.child, node.next
        node.child, node.next = None, None
        return node, child_node, next_node


nodes = [Node(i) for i in range(13)]

for i in range(1, 6):
    nodes[i].next = nodes[i + 1]
    nodes[i + 1].prev = nodes[i]

for i in range(7, 10):
    nodes[i].next = nodes[i + 1]
    nodes[i + 1].prev = nodes[i]

nodes[11].next = nodes[12]
nodes[12].prev = nodes[11]

nodes[3].child = nodes[7]
nodes[8].child = nodes[11]


def test(head: Node):
    flattened = Solution().flatten(head)
    it = flattened
    values: List[int] = []
    while it:
        values.append(it.val)
        it = it.next

    print(f'''\
Test #1
----------------------------------------------------
the flatten list is: {values}
''')


test(nodes[1])
