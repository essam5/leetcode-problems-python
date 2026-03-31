class Solution:
    def decodeString(self, s: str) -> str:
        """
        satck every letter till "]"
        adding new sub_str and loop with stack pop while stack[-1] not "["
        adding new sub_int (in case more than single number)
        after that adding to stack with sub_int * sub_str
        """
        stack = []
        for char in s: 
            if char != "]": # a,b,b,b,a,b,b,b,c 
                stack.append(char)
            else:
                # for sub_ string
                sub_str = ""
                while stack[-1] != "[":
                    sub_str = stack.pop() + sub_str # abbb
                stack.pop() # pop the "[" 

                # loop with int 
                sub_int = ""
                while stack and stack[-1].isdigit():
                    sub_int =  stack.pop() + sub_int # 2

                stack.append(int(sub_int) * sub_str) # abbbabbb

        return "".join(stack)                    
        