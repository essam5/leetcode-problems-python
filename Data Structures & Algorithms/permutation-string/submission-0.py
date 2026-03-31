class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        if we make loop with len() to count s1
        loop s2 , take slide index
        compare 
        
        """
        if len(s1) > len(s2):
            return False
        count_s1 = {}
        count_s2 = {}
        for letter in s1:
            count_s1[letter] = 1 + count_s1.get(letter, 0)

        for i in range(len(s1)):
            count_s2[s2[i]] = 1+count_s2.get(s2[i] , 0)

        if count_s1 == count_s2:
            return True

        left = 0

        for i in range(len(s1), len(s2)):
            print("count s2 before",count_s2, "the index is ", i)
            count_s2[s2[left]] -=1
            if count_s2[s2[left]] == 0:
                count_s2.pop(s2[left])
            count_s2[s2[i]] = 1 + count_s2.get(s2[i], 0)
            print("count s2 after ",count_s2)
            if count_s1 == count_s2:
                return True
            left += 1

        return False    


        