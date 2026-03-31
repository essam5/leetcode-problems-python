class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord("a")] +=1
            result[tuple(count)].append(word)
        return result.values()        
        