class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # first part build a graph 
        graph = defaultdict(set)
        for word in words:
            for w in word:
                graph[w] = set()

        # build an edges : 
        for i in range(len(words) -1):
            word_1, word_2= words[i], words[i+1]
            min_len = min(len(word_1), len(word_2))
            if word_1[:min_len] == word_2[:min_len] and len(word_1) > len(word_2):
                return ""

            for j in range(min_len):
                if word_1[j] !=word_2[j]:
                    graph[word_1[j]].add(word_2[j])
                    break
       
        # second part detect cycle like a sperate problem 

        # at this point we can start a problem like a graph problem with nodes 
        # like vertices and edges 
        visited = {} # assume 0 is unvisted, 1 is visiting --> can detect cycle 
        # 2 is visited 
        result = [] # we will add a value to this list like post order 
        # to get the right order like if we have graph like that: 
        # A  --> B --> c , and A --> c
        # if we dfs normally will be [A, c, B]  but we know that should A , B , C
        # so if we append to the list post order we will append like : 
        # C, B, A and reverse it to A, B, C


        def dfs(char):
            if char in visited:
                return visited[char] == 2 # other wise it is a cycle

            visited[char] = 1 # is visiting

            for nei in graph[char]:
                if not dfs(nei):
                    return False

            visited[char] = 2
            result.append(char) # post order

            return True        


        # loop at every letter 
        for char in graph:
            if not dfs(char):
                return ""

         # revers the result
        return "".join(result[::-1])        



        