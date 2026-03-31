class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}

        for index, num in enumerate(nums):
            sum_num = target - num
            if sum_num in seen:
                return [seen[sum_num], index]

            seen[num] = index
                    
