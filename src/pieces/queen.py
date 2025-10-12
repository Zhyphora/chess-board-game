class Piece:
    def __init__(self, color):
        self.color = color

from pieces.piece import Piece

class Queen(Piece):
    """Queen piece - combines rook and bishop movements."""
    
    def __init__(self, color):
        symbol = 'Q' if color == 'white' else 'q'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        # Can move like rook (straight line) or bishop (diagonal)
        is_straight = (start_row == end_row or start_col == end_col)
        is_diagonal = (row_diff == col_diff and row_diff > 0)
        
        if not (is_straight or is_diagonal):
            return False
        
        # Check if path is clear
        return self.is_path_clear(start, end, board)