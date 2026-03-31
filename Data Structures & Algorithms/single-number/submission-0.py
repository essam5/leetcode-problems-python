class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0 
        for num in nums:
            print('before  ', num, result)
            result = num ^ result
            print('afterr', num, result)

        return result     
        