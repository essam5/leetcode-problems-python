class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(index):
            if index >= len(s):
                res.append(part.copy())
                return

            for j in range(index, len(s)):
                if self.is_pal(s, index, j):
                    part.append(s[index:j+1])
                    dfs(j +1)
                    part.pop()

        dfs(0)

        return res

    def is_pal(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left +=1
            right -=1    


        return True                       

        