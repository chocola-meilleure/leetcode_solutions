class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        while head and head.next:
            p = head.next
            head.next = swapPairs(p.next) #다다음 노드의 swap실행한 결과를 현재 head에 연결한다   
            p.next = head
            return p #swap한 결과물 반환
        return head
