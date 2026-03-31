class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str += s + "-"
            print(new_str)
            
        return new_str    

    def decode(self, s: str) -> List[str]:
        print(s)
        start_point = 0
        end_point = 0
        new_list = []
        while end_point < len(s):
            if s[end_point] == "-":
                new_list.append(s[start_point:end_point])
                start_point = end_point + 1
            end_point +=1

        return new_list         

