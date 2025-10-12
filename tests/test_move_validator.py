import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from board.chess_board import ChessBoard


class TestMoveValidator(unittest.TestCase):
    """Test move validation logic."""
    
    def setUp(self):
        """Set up a fresh board for each test."""
        self.board = ChessBoard()
    
    def test_valid_pawn_move(self):
        """Test valid pawn move."""
        start = (1, 4)  # e2 (white pawn at row 1)
        end = (2, 4)    # e3 (move to row 2)
        
        is_valid, error = self.board.validate_move(start, end, 'white')
        self.assertTrue(is_valid, f"Valid pawn move should be accepted, error: {error}")
        self.assertEqual(error, "")
    
    def test_invalid_move_out_of_bounds(self):
        """Test move validation rejects out of bounds moves."""
        start = (0, 0)
        end = (8, 0)  # Out of bounds
        
        is_valid, error = self.board.validate_move(start, end, 'white')
        self.assertFalse(is_valid)
        self.assertIn("out of bounds", error.lower())
    
    def test_invalid_move_no_piece(self):
        """Test move validation rejects empty start position."""
        start = (3, 3)  # Empty square
        end = (4, 3)
        
        is_valid, error = self.board.validate_move(start, end, 'white')
        self.assertFalse(is_valid)
        self.assertIn("no piece", error.lower())
    
    def test_invalid_move_wrong_player(self):
        """Test move validation rejects moving opponent's piece."""
        start = (6, 4)  # Black pawn
        end = (5, 4)
        
        is_valid, error = self.board.validate_move(start, end, 'white')
        self.assertFalse(is_valid)
        self.assertIn("black", error.lower())
    
    def test_invalid_capture_own_piece(self):
        """Test move validation rejects capturing own piece."""
        start = (1, 4)  # White pawn at e2
        end = (1, 5)    # White pawn at f2
        
        is_valid, error = self.board.validate_move(start, end, 'white')
        self.assertFalse(is_valid)
        self.assertIn("own piece", error.lower())
    
    def test_invalid_move_for_piece_type(self):
        """Test move validation rejects invalid moves for piece type."""
        # Try to move pawn sideways
        start = (1, 4)  # White pawn at e2
        end = (1, 5)    # f2 (sideways)
        
        # First clear the destination
        self.board.board[1][5] = None
        
        is_valid, error = self.board.validate_move(start, end, 'white')
        self.assertFalse(is_valid)
        self.assertIn("invalid move", error.lower())
    
    def test_valid_knight_jump(self):
        """Test knight can jump over pieces."""
        start = (0, 1)  # White knight at b1
        end = (2, 2)    # c3
        
        is_valid, error = self.board.validate_move(start, end, 'white')
        self.assertTrue(is_valid, "Knight should be able to jump over pieces")
    
    def test_valid_capture(self):
        """Test valid capture move."""
        # Move white pawn to position where it can capture
        self.board.board[5][4] = 'P'  # White pawn at e3
        self.board.board[4][5] = 'p'  # Black pawn at f4
        
        start = (5, 4)
        end = (4, 5)
        
        is_valid, error = self.board.validate_move(start, end, 'white')
        self.assertTrue(is_valid, "Valid capture should be accepted")
    
    def test_rook_blocked_path(self):
        """Test rook cannot move through pieces."""
        start = (0, 0)  # White rook at a1
        end = (0, 5)    # f1
        
        # Pawn at b1 blocks the path
        is_valid, error = self.board.validate_move(start, end, 'white')
        self.assertFalse(is_valid)
    
    def test_bishop_blocked_path(self):
        """Test bishop cannot move through pieces."""
        start = (0, 2)  # White bishop at c1
        end = (3, 5)    # f4
        
        # Pawn at d2 blocks the path
        is_valid, error = self.board.validate_move(start, end, 'white')
        self.assertFalse(is_valid)


class TestBoundaryValidation(unittest.TestCase):
    """Test boundary and input validation."""
    
    def setUp(self):
        """Set up a fresh board for each test."""
        self.board = ChessBoard()
    
    def test_position_boundaries(self):
        """Test position boundary checking."""
        # Valid positions
        self.assertTrue(self.board.is_position_valid((0, 0)))
        self.assertTrue(self.board.is_position_valid((7, 7)))
        self.assertTrue(self.board.is_position_valid((3, 4)))
        
        # Invalid positions
        self.assertFalse(self.board.is_position_valid((-1, 0)))
        self.assertFalse(self.board.is_position_valid((0, -1)))
        self.assertFalse(self.board.is_position_valid((8, 0)))
        self.assertFalse(self.board.is_position_valid((0, 8)))
        self.assertFalse(self.board.is_position_valid((10, 10)))


if __name__ == '__main__':
    unittest.main()
