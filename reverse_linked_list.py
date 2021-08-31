# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
    
        new_head: Optional[ListNode] = None
            
        while head != None:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
        
        return new_head
    
#         values: List = []
#         new_head: Optional[ListNode] = head
        
#         while new_head != None:
#             values.append(new_head.val)
#             new_head = new_head.next
        
#         temp: Optional[ListNode] = ListNode(val = values[-1])
#         result = temp

#         i = 2
#         while i <= len(values):
#             temp.next = ListNode(val = values[-i])
#             temp = temp.next
#             i += 1
        
#         return result
        
        
