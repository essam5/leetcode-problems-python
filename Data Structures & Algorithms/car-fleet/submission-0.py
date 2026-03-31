class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
               # we need to get the time for every one 
               # if the last one has less than speed before the prev 
               # so that mean the prev can catch the last one that mean to be the fleet

               # first list the pair of position and speed
               # sort it and reverse it 
               # pop if the last two stack one greater than other so pop (FILO)

               pair = [[p, s] for p, s in zip(position, speed)]
               stack =[]

               for p, s in sorted(pair)[::-1]:
                    stack.append((target - p) / s)
                    if len(stack) >= 2 and stack[-1] <= stack[-2]:
                        stack.pop()

               return len(stack)        

        