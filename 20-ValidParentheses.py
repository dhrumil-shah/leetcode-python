class Solution:
    def isSameBracket(self, s: str) -> bool:
        return s =='[]' or s =='{}' or s =='()'
    
    def isValid(self, s: str) -> bool:
        bracket = []
        openParentheses = ['(', '{', '[']
        closeParentheses = [')', '}', ']']
        for i in range(len(s)):
            if (s[i] in openParentheses):
                bracket.append(s[i])
            if (s[i] in closeParentheses):
                if (len(bracket) == 0):
                    return False                
                # print(bracket[-1], s[i] )
                valid = self.isSameBracket( bracket.pop(-1) + s[i])
                if (not valid):
                    return valid
        return len(bracket) ==0
                
    def runtests(self):
        print(\
              self.isValid("") and \
              not self.isValid("]") and \
              not self.isValid("}") and \
              not self.isValid(")") and \
              not self.isValid("[") and \
              not self.isValid("{") and \
              not self.isValid("(") and \
              not self.isValid("(]") and \
              not self.isValid("({)}") and \
              self.isValid("()[]{}") and \
              self.isValid("{[]}") and \
              self.isValid("{}") and \
              self.isValid("[]") and \
              self.isValid("()") and \
              not self.isValid("([)])") and \
              not self.isValid("([())])")\
        )

sol = Solution()
sol.runtests()