class Solution:
    def trap(self, height: List[int]) -> int:
        # to get the space we need to see the right and left
        # and see the min of both 
        # and subtract from the i that we have 
        # so for every index we need the max at right and max at left
        # and get the min of both 
        # and subtract the height of the current index
        # so the eq --> min(max_right, max_left) - height[i]

        # first solution 
        # for every index get the max_right list 
        # same for left 
        # make another list to get this equation 
        n = len(height)

        # get the max_left list first
        max_left = [0]*n
        max_left[0] = height[0]

        for i in range(1,n):
            max_left[i] = max(height[i], max_left[i-1])

        # get the max_right list
        max_right = [0]*n
        max_right[n-1] = height[n-1]
        for i in range( n-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])  

        # make this eq --> min (max_left[i], max_right[i]) - height
        res = 0
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]




        return res            