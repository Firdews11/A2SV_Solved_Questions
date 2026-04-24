class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # so basically the Q is asking to flit O's to X, but the ones that u cant reach the border from, thats all
        # so first check the O's that are on the borders then we travers through them and place the O's that we got in a list, lets call is save zone or somthin, anyways so any O's other than those is gonna be flipped to X
        # to avoid extra space we can just change the O's to S then when traversing again we can just simply cahnge them back
        def dfs(row,col,board):
            board[row][col] = "S"
            direction = [(0,1),(1,0),(0,-1),(-1,0)]

            for r, c in direction:
                new_r, new_c = row + r, col + c

                if 0 <=new_r < rows and 0 <= new_c <colos:
                    if board[new_r][new_c] == "O":
                      dfs(new_r,new_c,board)

        rows, colos = len(board), len(board[0])
        for row in range(rows):
            for col in range(colos):
                 # checking top row,bottom row, left column, right column
                if row == 0 or row == rows-1 or col == 0 or col == colos-1:
                    if board[row][col] == "O":
                      dfs(row,col,board)
        # now lets change it back 
        for row in range(rows):
            for col in range(colos):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"
