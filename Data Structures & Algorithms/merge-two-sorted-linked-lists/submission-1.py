# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # first we need to use a dummy list to avoid any edge cases 
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        if list2:
            node.next = list2

        return dummy.next                    

















        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 # the small val
                list1 = list1.next # iterate the list
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next # to save the next val 

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next                    

        