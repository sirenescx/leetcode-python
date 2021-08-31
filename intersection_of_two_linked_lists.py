# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 1
        lenB = 1
        
        newA = headA
        newB = headB
        
        while newA.next != None:
            lenA += 1
            newA = newA.next
        
        while newB.next != None:
            lenB += 1
            newB = newB.next    
        
        if newA != newB:
            return None
        
        i = 0
        dist = abs(lenA - lenB)
        if lenA > lenB:         
            while i < dist:
                headA = headA.next
                i += 1
        else:
            while i < dist:
                headB = headB.next
                i += 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
        
