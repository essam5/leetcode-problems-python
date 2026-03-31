class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in num_set:
                length = 1

                while num + length in num_set:
                    length +=1 
                longest = max(length, longest)

        return longest             




















        # set the list 
        # check the starting number of sequence (num -1) if not in list
        # check for every num + 1 
        # adding length

        set_nums = set(nums)
        longest = 0

        for num in nums:
            if num -1 not in set_nums:
                length = 1
                while (num + length) in set_nums:
                    length += 1
                longest = max(length , longest)

        return longest             
        