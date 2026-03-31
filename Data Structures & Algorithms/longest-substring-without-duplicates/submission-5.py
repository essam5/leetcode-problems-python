class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        string_set = set()
        result = 1
        left = 0
        for letter in s:
            while letter in string_set:
                string_set.remove(s[left]) # first letter that repated
                left += 1
            string_set.add(letter)    
            
            print("letter is : ", letter)
            print("string set is :", string_set)
            print("res is :", result)
            result = max(result, len(string_set))


        return result            
        