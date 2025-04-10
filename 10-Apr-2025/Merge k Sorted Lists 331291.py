# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        # put the root of each list in the min heap
        for root in lists:
            if root is not None:
                heapq.heappush(minHeap, (root.val, id(root), root))

        # take the smallest(top) element from the min-heap and add it to the result
        # if top element has a next element add it to the heap
        res_head, res_tail = None, None

        while len(minHeap) > 0:
            value, _, node = heapq.heappop(minHeap)
            if res_head is None:
                res_head = node
                res_tail = node
            else:
                # make the new node the tail 
                # and make the newly inserted node the tail
                res_tail.next = node
                res_tail = res_tail.next

            if node.next is not None:
                heapq.heappush(minHeap, (node.next.val, id(node.next), node.next))

        return res_head