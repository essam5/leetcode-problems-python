class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1

        while left < right:

            while left < right and not s[left].isalnum(): left +=1
            while left < right and not s[right].isalnum(): right -=1

            if s[left].lower() != s[right].lower():
                return False

            left, right = left +1, right -1

        return True        














                      
        # reverse string 
        """
        new_s = ''
        for letter in s:
            if letter.isalnum():
                new_s += letter.lower()
        return new_s == new_s[::-1]  
        
        """
        l, r = 0, len(s) -1

        while l < r:
            while l < r and not self.is_alph_num(s[l]):
                l += 1
            while r > l and not self.is_alph_num(s[r]):
                r -= 1

            if s[r].lower() != s[l].lower():
                return False

            l += 1
            r -= 1
        return True                

    def is_alph_num(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))      

        
        