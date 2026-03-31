class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        [5,4,8,7,9]

        figure out the two largest number (x,y)
        if x == y , remove both 
        if x< y remove x, and make y = y-x 

        solution :
        heap the stones as max heap ( pop the first one and the heap[0])
        will be the second largest one 
        if both equal pop the both 
        if one less than other (make the greater (x-y))
        
        
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first- second)
        stones.append(0)
        return abs(stones[0])        
        