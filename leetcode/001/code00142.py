from typing import Optional, Union


class ListNode:
    def __init__(self, x, nextRef=None):
        self.val = x
        self.next: Optional[ListNode] = nextRef


class Solution:
    def detectCycle(self, head: ListNode) -> Union[ListNode, None]:
        single = head.next if head else None
        double = single.next if single else None
        while double is not None and single != double:
            single = single.next
            double = double.next
            if double:
                double = double.next
        if not double:
            return None

        single = head
        while single != double:
            single = single.next
            double = double.next
        return single

    def detectCycle2(self, head: ListNode) -> Union[ListNode, None]:
        single = head.next if head else None
        double = single.next if single else None
        while True:
            if not double or not double.next:
                return None
            double = double.next.next
            single = single.next
            if single == double:
                break

        single = head
        while single != double:
            single = single.next
            double = double.next
        return single


index = 0


def test(node: ListNode, expectedConnection: Union[ListNode, None]):
    global index
    index += 1
    connection = Solution().detectCycle2(node)
    print(f'''Test #{index}
----------------
expected connection matches: {connection is expectedConnection}
''')


node = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
connection = node.next
node.next.next.next.next = connection
test(node, connection)

node = ListNode(1, ListNode(2))
connection = node
node.next.next = connection
test(node, connection)

node = ListNode(1)
test(node, None)

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
connection = node.next.next
node.next.next.next.next.next.next = connection
test(node, connection)
