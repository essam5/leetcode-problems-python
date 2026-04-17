class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        word_map = defaultdict(list)
        wordList.append(beginWord) 

        for word in wordList: # o(n)
            for i in range(len(word)): # o(m) m is len of word
                pattern = word[:i] +"*" + word[i+1:]

                word_map[pattern].append(word)
        
        visited = set()
        visited.add(beginWord)
        queue = deque([beginWord])
        level = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return level

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]

                    for nei in word_map[pattern]:
                        if nei in visited:
                            continue
                        visited.add(nei)
                        queue.append(nei)

            level +=1            

        return 0 
         


        