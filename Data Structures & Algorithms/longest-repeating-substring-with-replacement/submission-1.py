class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the eq length - max_feq <= k
        left = 0
        max_freq = 0
        count = {}
        length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            while ((right - left) +1 - max_freq) > k:
                count[s[left]] -=1
                left +=1

            length = max(length, right- left +1)

        return length        

























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


           
        