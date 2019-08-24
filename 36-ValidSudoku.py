# prepare & validate rows
# prepare & validate columns
# prepare & validate 3*3
# determine if number is repeating or not
def isListValid(arrayList: List[str]) -> bool:
    #filter empty cell
    filtered = filter(isEmpty, arrayList)
    #if there is duplicate, return false
    final_list = []
    for variable in filtered:
        if variable in final_list:
            return False
        else:
            final_list.append(variable)
    return True

def isEmpty(variable):
    if (variable == "."):
        return False
    else:
        return True

class Solution:    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [[]]
        for i in range(0,9):
            # validating row
            if (isListValid(board[i]) == False):
                return False
            col = []
            for j in range(0,9):
                col.append(board[j][i])
            # validating column
            if (isListValid(col) == False):
                return False
            columns.append(col)
        
        for row in range (0,9,3):
            for cols in range(0,9,3):
                square = []
                for k in board[row][cols:cols+3]: square.append(k)
                for k in board[row+1][cols:cols+3]: square.append(k)
                for k in board[row+2][cols:cols+3]: square.append(k)
                if (isListValid(square) ==False) :
                    return False
        
        return True
