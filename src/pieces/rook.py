from pieces.piece import Piece

class Rook(Piece):
    """Rook piece - moves horizontally or vertically."""
    
    def __init__(self, color):
        symbol = 'R' if color == 'white' else 'r'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        
        # Must move in straight line (horizontal or vertical)
        if start_row != end_row and start_col != end_col:
            return False
        
        # Check if path is clear
        return self.is_path_clear(start, end, board)
