class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_arr = []
        left = 0
        for i in range(k, len(nums)+1):
            max_arr.append(max(nums[left:i])) 
            left +=1
        return max_arr    
        