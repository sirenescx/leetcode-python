# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class MergeIterator:
    def __init__(self, lists: List[Optional[ListNode]]):
        self.lists = lists
        self.heap = []
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(self.heap, (lists[i].val, i))
    
    def get_min_value(self) -> int:
        if self.heap == None or self.heap == []:
            return None
        
        value, index = heapq.heappop(self.heap)
        self.lists[index] = self.lists[index].next
        
        if self.lists[index] != None:
            heapq.heappush(self.heap, (self.lists[index].val, index))
        
        return value
        
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        it: MergeIterator = MergeIterator(lists)
        if it.heap == []:
            return None
        
        head = new_head = ListNode()
        
        while it.heap != []:
            value: int = it.get_min_value()
            head.next = ListNode(val = value)
            head = head.next
        
        return new_head.next
        
        
