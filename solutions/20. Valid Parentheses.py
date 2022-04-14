class Solution:
    def isValid(self, s: str) -> bool:
       
        d={}
        d[')']='('
        d['}']='{'
        d[']']='['
        stack=[]
        for char in s:
            if char not in d:
                stack.append(char)
            else:
                if len(stack)==0 or stack.pop()!=d[char]:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        
