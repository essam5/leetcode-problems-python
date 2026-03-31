class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        heapq.heapify(nums)
        max_length = 1
        sorted_list = []
        sorted_list.append(heapq.heappop(nums))
        while nums:
            print(sorted_list)
            if nums[0] == sorted_list[-1] + 1:
                sorted_list.append(heapq.heappop(nums))
                max_length = max(max_length, len(sorted_list))
            elif nums[0] == sorted_list[-1]:
                heapq.heappop(nums)
            else:
                sorted_list = []  
                sorted_list.append(heapq.heappop(nums))
        return max_length





























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
        