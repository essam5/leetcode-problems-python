class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
         negatice <--
         positive -->
         equal = destroy

         [-1, 4, 6]

         -1    4 
         <--   -->

         thats mean not coll 

         the condition 
         should be 
         positive first and negative second right ? 

         using stack to store the first one (that reperesent the positive)

         and when looping check if found negative and we have the previous one positive

         then do something ? 


         if we sum the two ===> if less than 0 
         that make the current win ? so destroy the one in the stack
         if they == 0 --> destroy both 
         if bigger than 0 that's mean in the stack win so we can make the curr
         like = 0 

        """

        stack = []

        for part in asteroids:
            while stack and part < 0 and stack[-1] >0:
                diff = part + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    part = 0
                else:
                    part = 0
                    stack.pop()

            if part:
                stack.append(part)

        return stack                       




