class Solution:
    def solve(self, board: List[List[str]]) -> None:
        component = set()
        visited = set()
        onBorder = False

        def findComponent(i, j):
            nonlocal component, onBorder
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
                return

            if board[i][j] == 'O':
                component.add((i, j))
            else:
                return
            
            if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                print(i, j)
                onBorder = True
            
            if (i + 1, j) not in component:
                findComponent(i + 1, j)
            if (i - 1, j) not in component:
                findComponent(i - 1, j)
            if (i, j + 1) not in component:
                findComponent(i, j + 1)
            if (i, j - 1) not in component:
                findComponent(i, j - 1)
        
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == 'O' and (i, j) not in visited:
                    findComponent(i, j)
                
                    print(component, onBorder)

                    if not onBorder:
                        while component:
                            i, j = component.pop()
                            visited.add((i, j))
                            board[i][j] = 'X'
                    else:
                        while component:
                            i, j = component.pop()
                            visited.add((i, j))
                        onBorder = False                

        