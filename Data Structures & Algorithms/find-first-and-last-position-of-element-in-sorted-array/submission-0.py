class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] < target:
                left = mid +1
            elif nums[mid] > target :
                right = mid -1
            else:
                first_index = mid
                last_index = mid
                # expand left
                while first_index - 1 >= 0 and nums[first_index - 1] == target:
                    first_index -= 1

                # expand right
                while last_index + 1 < len(nums) and nums[last_index + 1] == target:
                    last_index += 1

                return [first_index, last_index]

        return [-1,-1]                               

        