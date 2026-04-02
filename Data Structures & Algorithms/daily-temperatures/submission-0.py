class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair [temp, index]

        for index, temp in enumerate(temperatures):
            print(stack)
            while stack and stack[-1][0] < temp:

                curr_temp, curr_index = stack.pop()
                result[curr_index] = index - curr_index

            stack.append([temp, index])  

        return result      
        