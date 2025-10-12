from pieces.piece import Piece

class Bishop(Piece):
    """Bishop piece - moves diagonally."""
    
    def __init__(self, color):
        symbol = 'B' if color == 'white' else 'b'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        # Must move diagonally (same distance in both directions)
        if row_diff != col_diff or row_diff == 0:
            return False
        
        # Check if path is clear
        return self.is_path_clear(start, end, board)
