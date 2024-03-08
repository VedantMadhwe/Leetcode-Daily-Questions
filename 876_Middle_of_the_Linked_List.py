# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = end = head
        while end:
            if end and end.next:
                mid = mid.next
                end = end.next
            end = end.next
        return mid

