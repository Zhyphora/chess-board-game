from pieces.piece import Piece

class Knight(Piece):
    """Knight piece - moves in L-shape (2+1 squares)."""
    
    def __init__(self, color):
        symbol = 'N' if color == 'white' else 'n'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        # Knight moves in L-shape: 2 squares in one direction, 1 in perpendicular
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)
