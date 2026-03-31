class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        brute force loop from to max number of piles to get the k
        binary search loop also but consider l, r and mid
        after that check the number of hours by (p/k) but rounded up 

        
        """
        left, right = 1, max(piles)
        result = right

        while left <= right:
            k = (left+right) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                right = k -1
                result = min(result, k)
            else:
                left = k + 1         

        return result       
           


        