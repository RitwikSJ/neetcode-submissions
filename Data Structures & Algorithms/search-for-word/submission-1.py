class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def checkPath(board, partialWord, i, j):
            if not partialWord:
                return True
            
            print(partialWord, i, j)
            
            if j + 1 < len(board[i]):
                if board[i][j + 1] == partialWord[0]:
                    return checkPath(board, partialWord[1:], i, j + 1)
            
            if j - 1 >= 0:
                if board[i][j - 1] == partialWord[0]:
                    return checkPath(board, partialWord[1:], i, j - 1)
            
            if i - 1 >= 0:
                if board[i - 1][j] == partialWord[0]:
                    return checkPath(board, partialWord[1:], i - 1, j)

            if i + 1 < len(board):
                if board[i + 1][j] == partialWord[0]:
                    return checkPath(board, partialWord[1:], i + 1, j)
            
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if checkPath(board, word[1:], i, j):
                        return True
        
        return False

        