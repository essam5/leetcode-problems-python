class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 1- count
        # 2- length of wendow (right - left)+ 1
        # 3- check the max freq 
        # 4- if step2 - step3 =< k , that mean the result 
        # so if step4 greater than k , should remove the first element
        # and increament the left slide 
        count = {}
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] = 1+ count.get(s[right], 0)

            if (((right - left) + 1) - max(count.values()) ) >k:
                count[s[left]] -=1
                left +=1
            result = max(result,((right - left) + 1) )   

        return result     


           
        