class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count every element 
        # sort the element (put the count and index in arr and sorted it)
        # return till k element(by passing the pop element)

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

    

        