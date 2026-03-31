# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        hash_set = set()

        while head:
            if head.val in hash_set:
                return True
            hash_set.add(head.val)
            head = head.next

        return False        
        