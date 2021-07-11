# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None and l2 == None:
            return None
        res = head = ListNode()

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                res.val = l1.val
                res.next = ListNode()
                res = res.next
                l1 = l1.next
                continue
            if l1.val >= l2.val:
                res.val = l2.val
                res.next = ListNode()
                res = res.next
                l2 = l2.next
                continue

        if l1 == None and l2 != None:
            while l2 != None:
                res.val = l2.val
                if l2.next != None:
                    res.next = ListNode()
                res = res.next
                l2 = l2.next
        elif l1 != None and l2 == None:
            while l1 != None:
                res.val = l1.val
                if l1.next != None:
                    res.next = ListNode()
                res = res.next
                l1 = l1.next

        return head
