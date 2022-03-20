"""
lc link: https://leetcode.com/problems/design-tic-tac-toe/

This question is purely implementation with no algorithm involved
I personally feel like the O(1) check move solution is over-engineering
Thus I stick to O(n) regular solution in an interview
"""

class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for j in range(n)] for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        return self.check_winner(player, row, col)
    
    def check_winner(self, player, row, col):
        n = len(self.board)
        # first check for the previous row
        for j in range(n):
            if self.board[row][j] != player:
                break
        else:
            return player
        
        # then check for the previous col
        for i in range(n):
            if self.board[i][col] != player:
                break
        else:
            return player
        
        # check for diagonal 
        for i in range(n):
            if self.board[i][i] != player:
                break
        else:
            return player
        
        # check for anti diagonal 
        for i in range(n):
            if self.board[i][n-i-1] != player:
                break
        else:
            return player
        
        return 0