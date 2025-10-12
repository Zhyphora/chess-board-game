import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from board.chess_board import ChessBoard


class TestPieceMoves(unittest.TestCase):
    """Test valid and invalid moves for different pieces."""
    
    def setUp(self):
        """Set up empty board for each test."""
        self.board = ChessBoard()
        # Clear the board
        self.board.board = [[None for _ in range(8)] for _ in range(8)]
    
    def test_pawn_forward_one_square(self):
        """Test pawn moving forward one square."""
        pawn = Pawn('white')
        self.board.board[1][4] = 'P'  # White pawn at row 1 (real board position)
        
        # Valid move: row 1 to row 2
        self.assertTrue(pawn.is_valid_move((1, 4), (2, 4), self.board.board))
        
        # Invalid move: row 1 to row 4 (too far)
        self.assertFalse(pawn.is_valid_move((1, 4), (4, 4), self.board.board))
    
    def test_pawn_forward_two_squares_from_start(self):
        """Test pawn moving forward two squares from starting position."""
        pawn = Pawn('white')
        self.board.board[1][4] = 'P'  # White pawn at starting position (row 1)
        
        # Valid move: two squares forward from start
        self.assertTrue(pawn.is_valid_move((1, 4), (3, 4), self.board.board))
        
        # Invalid if piece in the way
        self.board.board[2][4] = 'p'
        self.assertFalse(pawn.is_valid_move((1, 4), (3, 4), self.board.board))
    
    def test_pawn_capture_diagonally(self):
        """Test pawn capturing diagonally."""
        pawn = Pawn('white')
        self.board.board[1][4] = 'P'  # White pawn at row 1
        self.board.board[2][5] = 'p'  # Black pawn at row 2, col 5
        
        # Valid diagonal capture
        self.assertTrue(pawn.is_valid_move((1, 4), (2, 5), self.board.board))
        
        # Invalid diagonal move without capture
        self.board.board[2][5] = None
        self.assertFalse(pawn.is_valid_move((1, 4), (2, 5), self.board.board))
    
    def test_rook_horizontal_movement(self):
        """Test rook moving horizontally."""
        rook = Rook('white')
        self.board.board[0][0] = 'R'  # White rook at a1
        
        # Valid horizontal move
        self.assertTrue(rook.is_valid_move((0, 0), (0, 5), self.board.board))
        
        # Invalid if piece blocking
        self.board.board[0][3] = 'P'
        self.assertFalse(rook.is_valid_move((0, 0), (0, 5), self.board.board))
    
    def test_rook_vertical_movement(self):
        """Test rook moving vertically."""
        rook = Rook('white')
        self.board.board[0][0] = 'R'  # White rook at a1
        
        # Valid vertical move
        self.assertTrue(rook.is_valid_move((0, 0), (5, 0), self.board.board))
        
        # Invalid diagonal move
        self.assertFalse(rook.is_valid_move((0, 0), (3, 3), self.board.board))
    
    def test_knight_l_shape_movement(self):
        """Test knight moving in L-shape."""
        knight = Knight('white')
        self.board.board[0][1] = 'N'  # White knight at b1
        
        # Valid L-shape moves
        self.assertTrue(knight.is_valid_move((0, 1), (2, 0), self.board.board))  # a3
        self.assertTrue(knight.is_valid_move((0, 1), (2, 2), self.board.board))  # c3
        
        # Invalid moves
        self.assertFalse(knight.is_valid_move((0, 1), (0, 3), self.board.board))  # straight
        self.assertFalse(knight.is_valid_move((0, 1), (2, 3), self.board.board))  # wrong distance
    
    def test_bishop_diagonal_movement(self):
        """Test bishop moving diagonally."""
        bishop = Bishop('white')
        self.board.board[0][2] = 'B'  # White bishop at c1
        
        # Valid diagonal move
        self.assertTrue(bishop.is_valid_move((0, 2), (3, 5), self.board.board))
        
        # Invalid if piece blocking
        self.board.board[1][3] = 'P'
        self.assertFalse(bishop.is_valid_move((0, 2), (3, 5), self.board.board))
        
        # Invalid non-diagonal move
        self.assertFalse(bishop.is_valid_move((0, 2), (0, 5), self.board.board))
    
    def test_queen_combined_movement(self):
        """Test queen moving like rook and bishop."""
        queen = Queen('white')
        self.board.board[0][3] = 'Q'  # White queen at d1
        
        # Valid horizontal move (like rook)
        self.assertTrue(queen.is_valid_move((0, 3), (0, 7), self.board.board))
        
        # Valid vertical move (like rook)
        self.assertTrue(queen.is_valid_move((0, 3), (5, 3), self.board.board))
        
        # Valid diagonal move (like bishop)
        self.assertTrue(queen.is_valid_move((0, 3), (3, 6), self.board.board))
        
        # Invalid knight-like move
        self.assertFalse(queen.is_valid_move((0, 3), (2, 4), self.board.board))
    
    def test_king_one_square_movement(self):
        """Test king moving one square in any direction."""
        king = King('white')
        self.board.board[0][4] = 'K'  # White king at e1
        
        # Valid one-square moves
        self.assertTrue(king.is_valid_move((0, 4), (0, 5), self.board.board))  # horizontal
        self.assertTrue(king.is_valid_move((0, 4), (1, 4), self.board.board))  # vertical
        self.assertTrue(king.is_valid_move((0, 4), (1, 5), self.board.board))  # diagonal
        
        # Invalid two-square move
        self.assertFalse(king.is_valid_move((0, 4), (0, 6), self.board.board))
        self.assertFalse(king.is_valid_move((0, 4), (2, 4), self.board.board))


class TestPieceSymbols(unittest.TestCase):
    """Test piece symbols are correct."""
    
    def test_white_piece_symbols(self):
        """Test white pieces have uppercase symbols."""
        self.assertEqual(Pawn('white').symbol, 'P')
        self.assertEqual(Rook('white').symbol, 'R')
        self.assertEqual(Knight('white').symbol, 'N')
        self.assertEqual(Bishop('white').symbol, 'B')
        self.assertEqual(Queen('white').symbol, 'Q')
        self.assertEqual(King('white').symbol, 'K')
    
    def test_black_piece_symbols(self):
        """Test black pieces have lowercase symbols."""
        self.assertEqual(Pawn('black').symbol, 'p')
        self.assertEqual(Rook('black').symbol, 'r')
        self.assertEqual(Knight('black').symbol, 'n')
        self.assertEqual(Bishop('black').symbol, 'b')
        self.assertEqual(Queen('black').symbol, 'q')
        self.assertEqual(King('black').symbol, 'k')


if __name__ == '__main__':
    unittest.main()
