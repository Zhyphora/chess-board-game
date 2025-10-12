from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King


class ChessBoard:
    """Represents the chess board and handles board operations."""
    
    def __init__(self):
        self.board = self._initialize_board()
        self.piece_map = self._create_piece_map()

    def _initialize_board(self):
        """Initialize an 8x8 chess board with pieces in starting positions."""
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Setup white pieces (row 0 and 1)
        board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        board[1] = ['P'] * 8
        
        # Setup black pieces (row 6 and 7)
        board[6] = ['p'] * 8
        board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        
        return board

    def _create_piece_map(self):
        """Create a mapping of symbols to piece objects for move validation."""
        return {
            'P': Pawn('white'), 'p': Pawn('black'),
            'R': Rook('white'), 'r': Rook('black'),
            'N': Knight('white'), 'n': Knight('black'),
            'B': Bishop('white'), 'b': Bishop('black'),
            'Q': Queen('white'), 'q': Queen('black'),
            'K': King('white'), 'k': King('black'),
        }

    def render(self):
        """Display the chess board with row and column labels."""
        print("\n  a b c d e f g h")
        print("  " + "-" * 15)
        for i, row in enumerate(self.board):
            row_str = f"{8 - i}|"
            for piece in row:
                row_str += piece if piece else '.'
                row_str += ' '
            print(row_str + f"|{8 - i}")
        print("  " + "-" * 15)
        print("  a b c d e f g h\n")

    def get_piece(self, position):
        """Get the piece at the given position."""
        row, col = position
        return self.board[row][col]

    def move_piece(self, start, end):
        """Move a piece from start to end position."""
        piece = self.board[start[0]][start[1]]
        self.board[end[0]][end[1]] = piece
        self.board[start[0]][start[1]] = None

    def is_position_valid(self, position):
        """Check if a position is within board boundaries."""
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8

    def is_king_captured(self, color):
        """Check if the king of the given color is still on the board."""
        king_symbol = 'K' if color == 'white' else 'k'
        for row in self.board:
            if king_symbol in row:
                return False
        return True

    def get_piece_color(self, symbol):
        """Get the color of a piece from its symbol."""
        if symbol is None:
            return None
        return 'white' if symbol.isupper() else 'black'

    def validate_move(self, start, end, current_player):
        """
        Validate if a move is legal.
        
        Args:
            start: Tuple (row, col) starting position
            end: Tuple (row, col) ending position
            current_player: 'white' or 'black'
            
        Returns:
            Tuple (is_valid, error_message)
        """
        # Check if positions are valid
        if not self.is_position_valid(start):
            return False, "Starting position is out of bounds"
        if not self.is_position_valid(end):
            return False, "Ending position is out of bounds"
        
        # Check if there's a piece at start position
        piece_symbol = self.get_piece(start)
        if piece_symbol is None:
            return False, "No piece at starting position"
        
        # Check if piece belongs to current player
        piece_color = self.get_piece_color(piece_symbol)
        if piece_color != current_player:
            return False, f"That piece belongs to {piece_color}, not {current_player}"
        
        # Check if trying to capture own piece
        target_symbol = self.get_piece(end)
        if target_symbol is not None:
            target_color = self.get_piece_color(target_symbol)
            if target_color == current_player:
                return False, "Cannot capture your own piece"
        
        # Check if move is valid for this piece type
        piece = self.piece_map.get(piece_symbol)
        if piece and not piece.is_valid_move(start, end, self.board):
            return False, f"Invalid move for {piece_symbol}"
        
        return True, ""