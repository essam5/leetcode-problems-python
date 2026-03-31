class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # make a list of min heap with len k (not greater than k)
        # because when we get the k largest element if the 
        # array len == 3 and k = 3 so the largest 3 element is the smallest one
        # so you can get by getting first element

        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]    
          

        

        
