class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # count = {}
        # for letter in s:
        #     if letter in count:
        #         count[letter] +=1
        #     else:
        #         count[letter] = 1

        # for letter in t:
        #     if letter in count:
        #         count[letter] -=1
        #     else:
        #         count[letter] = 1

        # for letter in count:
        #     if count[letter] != 0:
        #         return False
        #################
        count = [0] *26     #number of letters in english
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] +=1
            count[ord(t[i]) - ord("a")] -=1
        for value in count:
            if value != 0:
                return False            
        return True                
        