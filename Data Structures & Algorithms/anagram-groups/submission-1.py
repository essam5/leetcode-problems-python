class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        defaultdict(list)
        loop into the list 
        make count of 26 
        loop and add to our dict
        """
        output = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            output[tuple(count)].append(word)

        return list(output.values())        



























        result = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord("a")] +=1
            result[tuple(count)].append(word)
        return result.values()        
        