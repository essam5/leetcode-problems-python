class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left, right 
        # calculate the area 
        # shift one with the minmum 
        left, right = 0, len(heights) -1
        result = 0
        while right > left:
            area = min(heights[right], heights[left]) * (right - left)
            result = max(area, result)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -=1

        return result            

        