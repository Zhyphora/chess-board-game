from pieces.piece import Piece

class Pawn(Piece):
    """Pawn piece - moves forward, captures diagonally."""
    
    def __init__(self, color):
        symbol = 'P' if color == 'white' else 'p'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        
        # White pawns move down (increasing row), black pawns move up (decreasing row)
        # White pieces are at row 0-1, Black pieces are at row 6-7
        direction = 1 if self.color == 'white' else -1  # White moves down (+1), black moves up (-1)
        start_rank = 1 if self.color == 'white' else 6  # Starting row for pawns
        
        # Forward move (one square)
        if start_col == end_col and end_row == start_row + direction:
            return board[end_row][end_col] is None
        
        # Forward move (two squares from starting position)
        if start_col == end_col and start_row == start_rank and end_row == start_row + 2 * direction:
            middle_row = start_row + direction
            return board[middle_row][end_col] is None and board[end_row][end_col] is None
        
        # Diagonal capture
        if abs(end_col - start_col) == 1 and end_row == start_row + direction:
            target = board[end_row][end_col]
            if target is not None:
                target_color = 'white' if target.isupper() else 'black'
                return target_color != self.color
        
        return False
