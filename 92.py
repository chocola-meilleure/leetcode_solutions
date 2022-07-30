# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #예외 설정
        if not head or left == right:
            return head
        
        root = start = ListNode(None)
        root.next = head
        
        for _ in range(left- 1):
            start = start.next  #역순으로 바꿀 노드 이전의 노드를 start로 설정
        end = start.next       #역순 리스트의 끝이 될 부분을 end로 지정
        
        #노드 뒤집기
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
            
            
        return root.next
