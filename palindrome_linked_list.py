# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow: ListNode = head
        fast: ListNode = head
            
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        reversed_head: ListNode = None
        while slow != None:
            next_node = slow.next
            slow.next = reversed_head
            reversed_head = slow
            slow = next_node
 
        while reversed_head != None:
            if reversed_head.val != head.val:
                return False
            reversed_head = reversed_head.next
            head = head.next
            
        return True
            
