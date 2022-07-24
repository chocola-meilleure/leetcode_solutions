# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and (l1.val > l2.val)):
            #l1이 비어있거나 l2가 비어있지 않으면서 l1의 값이 l2보다 클 때
            l1, l2 = l2, l1
            
        if l1:  #l1이 비어있지 않을 때
            l1.next = self.mergeTwoLists(l1.next, l2)   
            
        return l1
    
