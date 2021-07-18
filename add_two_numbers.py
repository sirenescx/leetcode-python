# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        div = 0
        result = ListNode()
        head = result
        while l1 != None and l2 != None:
            num_sum = l1.val + l2.val + div
            digit = (num_sum) % 10
            if num_sum >= 10:
                div = (num_sum) // 10
            else:
                div = 0
            result.next = ListNode(digit)
            result = result.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            digit = (l1.val + div) % 10
            if l1.val + div >= 10:
                div = (l1.val + div) // 10
            else:
                div = 0   
            l1 = l1.next
            result.next = ListNode(digit)
            result = result.next
        
        while l2 != None:
            digit = (l2.val + div) % 10
            if l2.val + div >= 10:
                div = (l2.val + div) // 10
            else:
                div = 0  
            l2 = l2.next
            result.next = ListNode(digit)
            result = result.next
            
        if div != 0:
            result.next = ListNode(div)
            result = result.next
        
        return head.next
            
