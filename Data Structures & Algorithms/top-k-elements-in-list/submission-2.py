class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) +1
        freq_list = []

        for key, value in count.items():
            freq_list.append([-value, key])

        heapq.heapify(freq_list)

        c = 0
        res = []
        while c < k:
            value = heapq.heappop(freq_list)
            res.append(value[1])
            c +=1
        return res    



















        
        # count every element 
        # sort the element (put the count and index in arr and sorted it)
        # return till k element(by passing the pop element)
        """
        count = {}

        for num in nums:
            count[num] = 1+ count.get(num, 0)
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res     
        
        """    
        # solving it by bucket sort 
        """
        if we assume array of len nums , and the most repeated element will be count == len(nums)
        so we will create an array for the len(nums) and add to 
        every number the list of nums that repeated equal to the index
        ex : 
        Input: nums = [1,2,2,2,3,3], k = 2

        Output: [3,2]

        0 -- 1 -- 2 -- 3 -- 4 -- 5 -- 6
            [1]  [3]  [2]

        so the output will be [3, 2]    

        """

        count = {}

        for num in nums:
            count[num] = 1+ count.get(num, 0)

        freq = [[] for i in range(len(nums) +1)]
        print(len(freq))

        for num, cnt in count.items():
            freq[cnt].append(num)   

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



    

        