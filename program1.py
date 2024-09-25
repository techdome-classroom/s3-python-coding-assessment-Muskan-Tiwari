def isValid(s):
    stack=[]
    bracket={')' : '(' : '}' : '{' : ']' : '['}
    for char in s:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket.keys():
            if not stack or stack.pop()!= bracket[char]:
                return false
    return len(stack)==0







    



  

