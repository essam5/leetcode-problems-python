class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        # we just need the len of largest k, so we will never use
        # the min values that make the list has more than k len
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)


        # make a list of min heap with len k (not greater than k)
        # because when we get the k largest element if the 
        # array len == 3 and k = 3 so the largest third (at index 3) element is the smallest one
        # so you can get by getting first element
        # like [3, 5, 6] if sorted
        # the 3 or (third) largest element is 3 
        # that will be at first at the heap 

        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        # we need to pop again to still have the k len for the list of
        # min_heap but there an egde case that maybe we get the list
        # at first with less than k so we will not remove any thing 
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        print(self.min_heap[0])
        return self.min_heap[0]    



        
