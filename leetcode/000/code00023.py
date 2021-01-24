from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        size = self.initial_sort(lists)
        cur_min = 10 ** 4 + 1
        result_node = None
        last = None
        while size:
            index = 0
            for i in range(0, size):
                if lists[i].val <= lists[index].val:
                    index = i
                    if lists[i].val == cur_min:
                        break
            cur_min = lists[index].val
            if last:
                last.next = lists[index]
                last = last.next
            else:
                result_node = lists[index]
                last = result_node
            lists[index] = last.next
            if not last.next:
                size -= 1
                lists[index], lists[size] = lists[size], None
        return result_node

    def initial_sort(self, lists: List[ListNode]) -> int:
        """
        all valid values will be shifted to the left, all Nones (optional) - to the right.
        :param lists:
        :return: the new size of the array
        """
        put_i, take_i = 0, len(lists) - 1,
        while True:
            while put_i <= take_i and lists[put_i]:
                put_i += 1
            while take_i >= put_i and not lists[take_i]:
                take_i -= 1
            if put_i > take_i:
                break
            lists[put_i], lists[take_i] = lists[take_i], None
        return put_i

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        unboxed: List[int] = []
        for lst in lists:
            while lst is not None:
                unboxed.append(lst.val)
                lst = lst.next
        if not unboxed:
            return None
        unboxed.sort(reverse=True)
        result = ListNode(unboxed[0])

        for i in range(1, len(unboxed)):
            result = ListNode(unboxed[i], result)
        return result


indexes = [0]


def next_index() -> int:
    indexes[0] += 1
    return indexes[0]


def test(lists: List[ListNode]):
    initial_lists = list_of_nodes_to_list(lists)
    result = Solution().mergeKLists2(lists)
    print(f'''Test #{next_index()}
initial lists: {initial_lists};
       result: {node_to_list(result)}
''')


def list_of_nodes_to_list(lst: List[ListNode]):
    return list(map(node_to_list, lst))


def node_to_list(node: ListNode) -> List[int]:
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


test([])
test([None])
test([None, None])
test([ListNode(5)])
test([None, ListNode(5, ListNode(6))])
test([ListNode(6), ListNode(5), None, ListNode(5, ListNode(6))])
test([ListNode(2), None, ListNode(5), None, None, ListNode(3), None, None])
test([None, None, None, ListNode(2, ListNode(3, ListNode(5))), None, ListNode(-5, ListNode(-3, ListNode(-2, ListNode(3, ListNode(5))))), None, None, ListNode(-5, ListNode(5)), None, None])
