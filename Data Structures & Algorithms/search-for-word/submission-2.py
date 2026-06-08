class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        
        def checkPath(board, partialWord, i, j, path):
            if not partialWord:
                return True
            
            print(partialWord, i, j)
            
            if j + 1 < len(board[i]):
                if board[i][j + 1] == partialWord[0] and (i, j + 1) not in path:
                    path.add((i, j + 1))
                    if checkPath(board, partialWord[1:], i, j + 1, path):
                        return True
                    path.remove((i, j + 1))
            
            if j - 1 >= 0:
                if board[i][j - 1] == partialWord[0] and (i, j - 1) not in path:
                    path.add((i, j - 1))
                    if checkPath(board, partialWord[1:], i, j - 1, path):
                        return True
                    path.remove((i, j - 1))
            
            if i - 1 >= 0:
                if board[i - 1][j] == partialWord[0] and (i - 1, j) not in path:
                    path.add((i - 1, j))
                    if checkPath(board, partialWord[1:], i - 1, j, path):
                        return True
                    path.remove((i - 1, j))

            if i + 1 < len(board):
                if board[i + 1][j] == partialWord[0] and (i + 1, j) not in path:
                    path.add((i + 1, j))
                    if checkPath(board, partialWord[1:], i + 1, j, path):
                        return True
                    path.remove((i + 1, j))
            
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    path.add((i, j))
                    if checkPath(board, word[1:], i, j, path):
                        return True
                    path.remove((i, j))
        
        return False

        