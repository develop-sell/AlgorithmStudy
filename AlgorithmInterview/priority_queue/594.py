import heapq


def reconstructQueue(people: list[list[int]]) -> list[list[int]]:
    heap = []
    
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
        
    result = []
    
    while heap:
        person = heapq.heappop(heap) # pop 하는 순간 새로 힙을 만들어 정렬한다.
        result.insert(person[1], [-person[0], person[1]])
    
    return result

reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])