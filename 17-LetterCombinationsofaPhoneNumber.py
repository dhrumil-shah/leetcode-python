"""17. Letter Combinations of a Phone Number
"""

class Solution:
    
    def digitToLetter(self, s: str)-> List[str]:
        two = ['a', 'b', 'c']
        three = ['d','e','f']
        four = ['g','h','i']
        five = ['j', 'k', 'l']
        six = ['m','n','o']
        seven = ['p','q','r', 's']
        eight = ['t', 'u', 'v']
        nine = ['w','x','y','z']
        
        if (s == '2'):
            return two
        elif (s =="3"):
            return three
        elif (s =="4"):
            return four
        elif (s =="5"):
            return five
        elif (s =="6"):
            return six
        elif (s =="7"):
            return seven
        elif (s =="8"):
            return eight
        elif (s =="9"):
            return nine
        else:
            return []
        
    def generateCombinations(self, side1: List[str], side2: List[str]) -> List[str]:
        comb = []
        for i in range(len(side1)):
            for j in range(len(side2)):
                # string = side1[i] + side2[j]
                # print(string)
                comb.append(side1[i] + side2[j])
        
        return comb
        
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        if (length < 1):
            return []
        validLetters = ['2','3','4','5','6','7','8','9']
        comb = self.digitToLetter(digits[0])
        for i in range(1, length):
            if (digits[i] not in validLetters):
                print("returning blank")
                return []
            else:
                comb = self.generateCombinations(comb, self.digitToLetter(digits[i]))
        return comb

    
    def runtest(self):
        if (self.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"] \
            and self.letterCombinations("27") == ["ap","aq","ar","as","bp","bq","br","bs","cp","cq","cr","cs"] \
           and self.letterCombinations("22") == ["aa","ab","ac","ba","bb","bc","ca","cb","cc"] \
            and self.letterCombinations("234") == ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"] \
           ):
            print(True)
        else:
            print(False)
            
sol = Solution()
sol.runtest()