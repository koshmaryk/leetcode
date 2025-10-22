class Solution:
    import heapq

    '''
    2 ladders
    3 bricks

    2,4,12,5,10,6,7

    --------------
    2 ladders
    0 bricks

    heap = [1,5,8]

    '''
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
            
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            
                if bricks < 0:
                    return i
                    
        return n - 1
                