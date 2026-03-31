class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointer but like sliding 
        # save a set and get the max_length of this set every loop
        # inside it check if we found the char in set
        # remove it and increment the left 
        if len(s) == 0:
            return 0
        left, right = 0, 1
        visit = set(s[left])
        max_length = len(visit)

        while right < len(s):
            while s[right] in visit:
                visit.remove(s[left])
                left +=1
            visit.add(s[right])
            max_length = max(max_length, len(visit))
            right +=1    

        return max_length    



















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
        