class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair : [index, height]
        max_area = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                pop_index, pop_height = stack.pop()
                max_area = max(max_area, pop_height *(index - pop_index))

                start = pop_index

            stack.append([start, height])  

        for index, height in stack:
            # the rest can compare with the all len of heights
            max_area =   max(max_area, height *(len(heights) - index))

        return max_area       
        