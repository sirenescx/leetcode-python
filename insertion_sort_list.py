# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        temporary_head: Optional[ListNode] = ListNode(-5000 - 1)
        sorted_head: Optional[ListNode] = temporary_head
        
        while head != None:
            if head.val >= temporary_head.val:
                temporary_head.next = ListNode(head.val)
                temporary_head = temporary_head.next
            else:
                start: Optional[ListNode] = sorted_head
                while start.next != None and start.next.val < head.val:
                    start = start.next
                
                tail: Optional[ListNode] = start.next
                start.next = ListNode(head.val)
                start = start.next
                start.next = tail
                
            head = head.next
        
        return sorted_head.next
