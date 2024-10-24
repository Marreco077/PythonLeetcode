# 999. Available Captures for Rook
# You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 
# 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.
# A rook can move any number of squares horizontally or vertically (up, down, left, right) 
# until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.
# Note: A rook cannot move through other pieces, such as bishops or pawns. 
# This means a rook cannot attack a pawn if there is another piece blocking the path.
# Return the number of pawns the white rook is attacking.


from typing import List

def numRookCaptures(board: List[List[str]]) -> int:
    



board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
         [".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

numRookCaptures(board)