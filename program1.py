class Solution(object):
    def isValid(self,s):
     stack=[]
     bracket={')' : '(' : '}' : '{' : ']' : '['}
     for char in s:
         if char in bracket.values():
             stack.append(char)
         elif char in bracket.keys():
             if not stack or stack.pop()!= bracket[char]:
                 print(False)
                 return 
     print(len(stack)==0)








    



  

