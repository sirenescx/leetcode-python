class Solution(object):
    
    def isEmpty(self, stack):
        return len(stack) == 0
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c == '}':
                if not self.isEmpty(stack) and stack[-1] == '{':
                    stack.pop()
                else: 
                    return False
            elif c == ')':
                if not self.isEmpty(stack) and stack[-1] == '(':
                    stack.pop()
                else: 
                    return False
            elif c == ']':
                if not self.isEmpty(stack) and stack[-1] == '[':
                    stack.pop() 
                else: 
                    return False
            
        return self.isEmpty(stack)
