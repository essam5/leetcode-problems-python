class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        add seen set()
        to check if you already added to it that's mean 
        there are duplicated elements
        check if len(seen) > k remove the i element 
        becaue :
        k greater than array size ➔ Window covers entire array
        look at this to understand 
        https://chatgpt.com/c/686fbdc2-9130-800d-ac51-ec0ba374ce0e
        """
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

            if len(seen) > k:
                seen.remove(nums[i-k])


        return False            


        