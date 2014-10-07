#!/usr/bin/env python
# Evaluate Reverse Polish Notation
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalCal(self,x,y,calcu):
        x = int(x)
        y = int(y)
        
        if calcu == "+":
            return  x + y
        elif calcu == "-":
            return x - y 
        elif calcu == "*":
            return x * y
        elif calcu == "/":
            if x * y < 0:
                return -( -x / y )
            else:
                return x / y
        else:
            return 0
            
    def evalRPN(self, tokens):
        j=0
        result=tokens[0]
        while(len( tokens ) != 1):
            if tokens[j] in ("+","-","*","/"):
                calcu = tokens[j]
                x = tokens.pop(j-2)
                y = tokens.pop(j-2)
                tokens[j-2] = self.evalCal(x,y,calcu)
                j = j - 1
            else:
                j = j + 1
        return int( tokens[0] )

c = Solution()
print c.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
