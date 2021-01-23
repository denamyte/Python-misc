from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # todo Completely remaster this method with moving all non-None values to the left
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result_ptr = None
        last = None
        for i in range(len(lists) - 1, -1, -1):
            if not lists[i]:
                del lists[i]
        while len(lists):
            index = 0  # the index of the node with the smallest value
            for i in range(1, len(lists)):
                if lists[i].val is not None and lists[i].val < lists[index].val:
                    index = i
            if last:
                last.next = lists[index]
                last = lists[index]
            else:
                result_ptr = lists[index]
                last = lists[index]
            if last.next:
                lists[index] = last.next
            else:
                del lists[index]
        return result_ptr

    def mergeKLists_new(self, lists: List[ListNode]) -> ListNode:
        size = self.remove_initial_nones(lists)

    def remove_initial_nones(self, lists: List[ListNode]) -> int:
        '''
        :param lists: all not-none values will be on the left, all none values - on the right
        :return: the new size of array
        '''
        # todo Implement this method
        length = len(lists)
        put_i, take_i = 0, length - 1,
        # while put_i <= take_i:
        while put_i <= take_i:
            while lists[put_i] and put_i < length - 1:
                put_i += 1
            while not lists[take_i] and take_i >= 0:
                    take_i -= 1
            if put_i > take_i:
                break
            lists[put_i], lists[take_i] = lists[take_i], None
        return put_i



def test(index: int, lists: List[ListNode]):
    lists_of_ints = list(map(node_to_list, lists))
    result = node_to_list(Solution().mergeKLists_new(lists))
    print(f'''Test #{index}
lists:  {lists_of_ints};
result: {result}
''')


def node_to_list(node: ListNode) -> List[int]:
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


# # [[1,4,5],[1,3,4],[2,6]]
# lists: List[ListNode] = [
#     ListNode(1, ListNode(4, ListNode(5))),
#     ListNode(1, ListNode(3, ListNode(4))),
#     ListNode(2, ListNode(6))
# ]
# test(1, lists)

# lists = []
# test(2, lists)

# lists = [None]
# test(3, lists)

lists = [None, None]
test(4, lists)

# lists = [ListNode(6), None, None, ListNode(1, ListNode(5, ListNode(7))),
#          None, ListNode(-1, ListNode(9)), None, None, ListNode(10), ListNode(-10)]
# test(5, lists)
