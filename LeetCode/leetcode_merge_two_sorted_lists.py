# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        crnt = dummy_node
        while l1 and l2:
            if l1.val <= l2.val:
                crnt.next = l1
                l1 = l1.next
                crnt = crnt.next
            else:
                crnt.next = l2
                l2 = l2.next
                crnt = crnt.next
        if l1:
            crnt.next = l1
        else: 
            crnt.next = l2
        
        return dummy_node.next
