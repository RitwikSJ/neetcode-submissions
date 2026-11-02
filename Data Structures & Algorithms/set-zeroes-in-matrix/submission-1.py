class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def flip(i, j):
            # print(i, j)
            if matrix[i][j] == 0 or matrix[i][j][-1] == "c":
                for k in range(len(matrix[0])):
                    if type(matrix[i][k]) == int:
                        matrix[i][k] = str(matrix[i][k]) + " r"
                    elif matrix[i][k][-1] == "c":
                        matrix[i][k] = "rc"

            if matrix[i][j] == 0 or matrix[i][j][-1] == "r":
                for k in range(len(matrix)):
                    if type(matrix[k][j]) == int:
                        matrix[k][j] = str(matrix[k][j]) + " c"
                    elif matrix[k][j][-1] == "r":
                        matrix[k][j] = "rc"
            
            # print(matrix)
                                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    flip(i, j)
                elif type(matrix[i][j]) == str and matrix[i][j][:2] == "0 ":
                    flip(i, j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if type(matrix[i][j]) == str:
                    matrix[i][j] = 0