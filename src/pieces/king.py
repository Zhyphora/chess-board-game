from pieces.piece import Piece

class King(Piece):
    """King piece - moves one square in any direction."""
    
    def __init__(self, color):
        symbol = 'K' if color == 'white' else 'k'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        # King can move one square in any direction
        return row_diff <= 1 and col_diff <= 1 and (row_diff > 0 or col_diff > 0)