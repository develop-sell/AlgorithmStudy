import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def mergeKLists(lists) -> ListNode:
    root = result = ListNode(None)
    heap = []
    
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i][0], i, lists[i]))
    
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]
        
        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
            
    return root.next

mergeKLists([[1,4,5], [1,3,4], [2,6]])