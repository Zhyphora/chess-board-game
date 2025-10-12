import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from board.chess_board import ChessBoard


class TestChessBoard(unittest.TestCase):
    """Test board initialization and basic operations."""
    
    def setUp(self):
        """Set up a fresh board for each test."""
        self.board = ChessBoard()
    
    def test_board_initialization(self):
        """Test that board is initialized correctly with all pieces."""
        # Test white pieces (row 0)
        self.assertEqual(self.board.get_piece((0, 0)), 'R', "White rook at a1")
        self.assertEqual(self.board.get_piece((0, 1)), 'N', "White knight at b1")
        self.assertEqual(self.board.get_piece((0, 2)), 'B', "White bishop at c1")
        self.assertEqual(self.board.get_piece((0, 3)), 'Q', "White queen at d1")
        self.assertEqual(self.board.get_piece((0, 4)), 'K', "White king at e1")
        self.assertEqual(self.board.get_piece((0, 5)), 'B', "White bishop at f1")
        self.assertEqual(self.board.get_piece((0, 6)), 'N', "White knight at g1")
        self.assertEqual(self.board.get_piece((0, 7)), 'R', "White rook at h1")
        
        # Test white pawns (row 1)
        for col in range(8):
            self.assertEqual(self.board.get_piece((1, col)), 'P', f"White pawn at column {col}")
        
        # Test empty squares (rows 2-5)
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(self.board.get_piece((row, col)), f"Empty square at ({row},{col})")
        
        # Test black pawns (row 6)
        for col in range(8):
            self.assertEqual(self.board.get_piece((6, col)), 'p', f"Black pawn at column {col}")
        
        # Test black pieces (row 7)
        self.assertEqual(self.board.get_piece((7, 0)), 'r', "Black rook at a8")
        self.assertEqual(self.board.get_piece((7, 1)), 'n', "Black knight at b8")
        self.assertEqual(self.board.get_piece((7, 2)), 'b', "Black bishop at c8")
        self.assertEqual(self.board.get_piece((7, 3)), 'q', "Black queen at d8")
        self.assertEqual(self.board.get_piece((7, 4)), 'k', "Black king at e8")
        self.assertEqual(self.board.get_piece((7, 5)), 'b', "Black bishop at f8")
        self.assertEqual(self.board.get_piece((7, 6)), 'n', "Black knight at g8")
        self.assertEqual(self.board.get_piece((7, 7)), 'r', "Black rook at h8")
    
    def test_board_dimensions(self):
        """Test that board has correct dimensions."""
        self.assertEqual(len(self.board.board), 8, "Board should have 8 rows")
        for row in self.board.board:
            self.assertEqual(len(row), 8, "Each row should have 8 columns")
    
    def test_piece_colors(self):
        """Test that pieces have correct colors."""
        # White pieces should be uppercase
        self.assertEqual(self.board.get_piece_color('P'), 'white')
        self.assertEqual(self.board.get_piece_color('K'), 'white')
        self.assertEqual(self.board.get_piece_color('Q'), 'white')
        
        # Black pieces should be lowercase
        self.assertEqual(self.board.get_piece_color('p'), 'black')
        self.assertEqual(self.board.get_piece_color('k'), 'black')
        self.assertEqual(self.board.get_piece_color('q'), 'black')
        
        # None should return None
        self.assertIsNone(self.board.get_piece_color(None))
    
    def test_move_piece(self):
        """Test moving a piece."""
        # Move white pawn from e2 to e4
        start = (1, 4)
        end = (3, 4)
        
        piece = self.board.get_piece(start)
        self.assertEqual(piece, 'P')
        
        self.board.move_piece(start, end)
        
        # Check that piece moved
        self.assertIsNone(self.board.get_piece(start))
        self.assertEqual(self.board.get_piece(end), 'P')
    
    def test_position_validation(self):
        """Test position boundary validation."""
        self.assertTrue(self.board.is_position_valid((0, 0)))
        self.assertTrue(self.board.is_position_valid((7, 7)))
        self.assertTrue(self.board.is_position_valid((3, 4)))
        
        self.assertFalse(self.board.is_position_valid((-1, 0)))
        self.assertFalse(self.board.is_position_valid((0, -1)))
        self.assertFalse(self.board.is_position_valid((8, 0)))
        self.assertFalse(self.board.is_position_valid((0, 8)))
    
    def test_king_capture_detection(self):
        """Test king capture detection."""
        # Initially both kings should be present
        self.assertFalse(self.board.is_king_captured('white'))
        self.assertFalse(self.board.is_king_captured('black'))
        
        # Remove white king
        self.board.board[0][4] = None
        self.assertTrue(self.board.is_king_captured('white'))
        self.assertFalse(self.board.is_king_captured('black'))
        
        # Remove black king
        self.board.board[7][4] = None
        self.assertTrue(self.board.is_king_captured('black'))


if __name__ == '__main__':
    unittest.main()
