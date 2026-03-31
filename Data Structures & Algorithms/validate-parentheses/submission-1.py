class Solution:
    def isValid(self, s: str) -> bool:
        ref = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        visit = []

        for br in s:
            if br in ref:
                if visit and visit[-1] == ref[br]:
                    visit.pop()
                else:
                    return False    
            else:
                visit.append(br)    


        return True if not visit else False            

        