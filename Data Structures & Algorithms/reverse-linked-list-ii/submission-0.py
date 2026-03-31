# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1   2   3   4   5
        #     2   3   4   5

        # 2   1   3   4   5

        # 2   1   4   5

        # 3   2   1   4   5

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # hold the list after prev
        curr = prev.next
        # reverse the sublist
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next        
        



        