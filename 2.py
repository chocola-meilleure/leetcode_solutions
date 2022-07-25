# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
    def toList(self, node: ListNode) -> List:
        list: List =[]
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev    #r의 원소 하나를 끊어내고 역순 연결리스트 prev의 맨 앞에 붙인다
            prev = node #역순 연결 리스트를 prev에 저장
            
        return node
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:   
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(i) for i in a)) + int(''.join(str(j) for j in b))
        
        return self.toReversedLinkedList(str(resultStr))
        
