from typing import Union


class Node:

    def __init__(self, val: int, nxt=None):
        self.val: int = val
        self.next: Node = nxt


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head: Union[Node, None] = None
        self.size: int = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        n = self.getNodeAtIndex(index)
        return n.val if n else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.head = Node(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        n = self.getNodeAtIndex(self.size - 1)
        if not n:
            self.addAtHead(val)
        else:
            n.next = Node(val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or self.size < index:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            prev = self.getNodeAtIndex(index - 1)
            nxt = prev.next
            n = Node(val, nxt)
            prev.next = n
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or self.size <= index:
            return

        if index == 0:
            if self.head:
                self.head = self.head.next
                self.size -= 1
            return

        prev = self.getNodeAtIndex(index - 1)
        prev.next = prev.next.next
        self.size -= 1

    def getNodeAtIndex(self, index: int) -> Union[Node, None]:
        if index < 0 or self.size <= index:
            return None
        cur_i, n = 0, self.head
        while cur_i < index:
            n = n.next
            cur_i += 1
        return n


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


def t1():
    lst = MyLinkedList()
    lst.addAtHead(1)
    lst.addAtTail(3)
    lst.addAtIndex(1, 2)    # linked list becomes 1->2->3
    print(lst.get(1))       # return 2
    lst.deleteAtIndex(1)    # now the linked list is 1->3
    print(lst.get(1))       # return 3


def t2():
    lst = MyLinkedList()
    lst.addAtTail(1)  # 1
    lst.addAtTail(2)  # 1->2
    lst.addAtTail(3)  # 1->2->3
    lst.addAtTail(4)  # 1->2->3->4
    print(lst.get(1))  # 2
    print(lst.get(3))  # 4
    print(lst.get(-1))  # -1
    print(lst.get(4))   # -1
    print_list(lst)


def t3():
    lst = MyLinkedList()
    lst.addAtIndex(0, 2)  # 2
    lst.addAtTail(3)      # 2->3
    lst.addAtHead(1)      # 1->2->3
    lst.addAtTail(5)      # 1->2->3->5
    lst.addAtIndex(3, 4)  # 1->2->3->4->5
    lst.addAtIndex(5, 6)  # 1->2->3->4->5->6
    print_list(lst)


def t4():
    lst = MyLinkedList()
    for i in range(10):
        lst.addAtIndex(0, i)
    print_list(lst)
    for _ in range(20):
        lst.deleteAtIndex(2)
    print_list(lst)
    lst.deleteAtIndex(-2)
    lst.deleteAtIndex(5)
    print_list(lst)

    for i in range(8):
        lst.addAtIndex(2, i)
    print_list(lst)
    for _ in range(2):
        lst.deleteAtIndex(0)
        lst.deleteAtIndex(lst.size - 1)
    print_list(lst)
    for i in range(2):
        lst.addAtHead(8 + i)
        lst.addAtTail(1 - i)
    print_list(lst)
    print(lst.size)


def print_list(lst: MyLinkedList):
    print([lst.get(i) for i in range(-1, lst.size + 1)])


t4()
