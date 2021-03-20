from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        SURVIVER = "S"
        if len(board) < 1:
            return
        if len(board[0]) < 1:
            return
        # 找出与边界交互的O
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                self.markUnChange(i, j, board)
        for n in [0, len(board[0])-1]:
            for m in range(len(board)):
                self.markUnChange(m, n, board)
        for p in range(len(board)):
            for k in range(len(board[0])):
                if board[p][k] == 'O':
                    board[p][k] = 'X'
                elif board[p][k] == SURVIVER:
                    board[p][k] = 'O'

    def markUnChange(self, i, j, board):
        if board[i][j] == 'O':
            board[i][j] = "S"
            temp = [[i, j]]
            index = 0
            while index < len(temp):
                position = temp[index]
                h = position[0]
                w = position[1]
                self.around(h, w, board, temp)
                index += 1

    def around(self, h, w, board, queue):
        if h > 0 and board[h-1][w] == 'O':
            board[h-1][w] = "S"
            queue.append([h-1, w])
        if w > 0 and board[h][w-1] == 'O':
            board[h][w-1] = "S"
            queue.append([h, w-1])
        if h < len(board)-1 and board[h+1][w] == 'O':
            board[h+1][w] = "S"
            queue.append([h+1, w])
        if w < len(board[0])-1 and board[h][w+1] == 'O':
            board[h][w+1] = "S"
            queue.append([h, w+1])


board = [["O","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","O","O","O","O"],["O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","X","O","X","O","O","O","O","X","O","O","X","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","X","O"],["O","X","X","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","X","O","O","O","O","O","O","X","O","O","O","O","O","X","X","O"],["O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","X","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],["O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","O","O","O","O","X","X","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O"],["O","O","O","O","X","O","O","O","O","O","O","O","O","X","O","O","O","O","O","X"],["O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","X","O","X","O","O"],["O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","X","X","O","O","O","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]]
Solution().solve(board)
print(board)