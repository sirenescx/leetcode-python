# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = ListNode()
        new_head = cur
        while head != None:
            if head.val != val:
                cur.next = ListNode()
                cur = cur.next
                cur.val = head.val
            head = head.next
        return new_head.next
