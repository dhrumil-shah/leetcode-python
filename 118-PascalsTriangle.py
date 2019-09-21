"""
118. Pascal's Triangle
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        retList = []
        firstTwo = [[1], [1,1]]
        if numRows == 1:
            retList.append(firstTwo[0])
        if numRows ==2:
            retList.append(firstTwo[0])
            retList.append(firstTwo[1])
        
        if (numRows >= 3): 
            retList.append(firstTwo[0])
            retList.append(firstTwo[1])
            print(numRows)
            for i in range(2,numRows):
                retList.append(self.prepareList(i, retList))
        return retList
                
    def prepareList(self, num, retList: List[List[int]]) -> List[int]:
        newList = [1]*(num+1)
        numbersAbove = retList[num-1]
        length = len(numbersAbove)
        for i in range(1, length):
            newList[i] = numbersAbove[i-1]+numbersAbove[i]
        return newList
        
