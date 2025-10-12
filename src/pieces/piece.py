class Piece:
    """Base class for all chess pieces."""
    
    def __init__(self, color, symbol):
        """
        Initialize a piece.
        
        Args:
            color: 'white' or 'black'
            symbol: Single character representation (uppercase for white, lowercase for black)
        """
        self.color = color
        self.symbol = symbol

    def is_valid_move(self, start, end, board):
        """
        Check if a move from start to end is valid for this piece.
        
        Args:
            start: Tuple (row, col) starting position
            end: Tuple (row, col) ending position
            board: The chess board (2D list)
            
        Returns:
            Boolean indicating if move is valid
        """
        raise NotImplementedError("Subclasses must implement is_valid_move")

    def is_path_clear(self, start, end, board):
        """
        Check if path between start and end is clear (no pieces blocking).
        Used for rook, bishop, and queen moves.
        """
        start_row, start_col = start
        end_row, end_col = end
        
        row_dir = 0 if start_row == end_row else (1 if end_row > start_row else -1)
        col_dir = 0 if start_col == end_col else (1 if end_col > start_col else -1)
        
        current_row = start_row + row_dir
        current_col = start_col + col_dir
        
        while (current_row, current_col) != (end_row, end_col):
            if board[current_row][current_col] is not None:
                return False
            current_row += row_dir
            current_col += col_dir
        
        return True

    def __str__(self):
        return self.symbol