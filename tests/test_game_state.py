import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from game.game_state import GameState
from board.chess_board import ChessBoard


class TestGameState(unittest.TestCase):
    """Test game state management."""
    
    def setUp(self):
        """Set up a fresh game state for each test."""
        self.game_state = GameState()
    
    def test_initial_state(self):
        """Test initial game state."""
        self.assertEqual(self.game_state.current_player, 'white')
        self.assertFalse(self.game_state.is_game_over)
        self.assertIsNone(self.game_state.winner)
        self.assertEqual(len(self.game_state.move_history), 0)
    
    def test_switch_player(self):
        """Test player switching."""
        self.assertEqual(self.game_state.current_player, 'white')
        
        self.game_state.switch_player()
        self.assertEqual(self.game_state.current_player, 'black')
        
        self.game_state.switch_player()
        self.assertEqual(self.game_state.current_player, 'white')
    
    def test_set_game_over(self):
        """Test setting game over state."""
        self.assertFalse(self.game_state.is_game_over)
        
        self.game_state.set_game_over('white')
        self.assertTrue(self.game_state.is_game_over)
        self.assertEqual(self.game_state.winner, 'white')
    
    def test_add_move_to_history(self):
        """Test adding moves to history."""
        self.assertEqual(len(self.game_state.move_history), 0)
        
        self.game_state.add_move((6, 4), (4, 4), 'P')
        self.assertEqual(len(self.game_state.move_history), 1)
        
        move = self.game_state.move_history[0]
        self.assertEqual(move['start'], (6, 4))
        self.assertEqual(move['end'], (4, 4))
        self.assertEqual(move['piece'], 'P')
        self.assertEqual(move['player'], 'white')
    
    def test_reset_game(self):
        """Test resetting game state."""
        # Make some changes
        self.game_state.switch_player()
        self.game_state.add_move((6, 4), (4, 4), 'P')
        self.game_state.set_game_over('black')
        
        # Reset
        self.game_state.reset_game()
        
        # Check everything is reset
        self.assertEqual(self.game_state.current_player, 'white')
        self.assertFalse(self.game_state.is_game_over)
        self.assertIsNone(self.game_state.winner)
        self.assertEqual(len(self.game_state.move_history), 0)


class TestWinCondition(unittest.TestCase):
    """Test win condition (king capture)."""
    
    def setUp(self):
        """Set up board and game state for each test."""
        self.board = ChessBoard()
        self.game_state = GameState()
    
    def test_initial_no_winner(self):
        """Test that initially there's no winner."""
        self.assertFalse(self.board.is_king_captured('white'))
        self.assertFalse(self.board.is_king_captured('black'))
        self.assertFalse(self.game_state.is_game_over)
    
    def test_white_king_captured(self):
        """Test detection of white king capture."""
        # Remove white king
        self.board.board[0][4] = None
        
        self.assertTrue(self.board.is_king_captured('white'))
        self.assertFalse(self.board.is_king_captured('black'))
        
        # Set game over
        self.game_state.set_game_over('black')
        self.assertTrue(self.game_state.is_game_over)
        self.assertEqual(self.game_state.winner, 'black')
    
    def test_black_king_captured(self):
        """Test detection of black king capture."""
        # Remove black king
        self.board.board[7][4] = None
        
        self.assertTrue(self.board.is_king_captured('black'))
        self.assertFalse(self.board.is_king_captured('white'))
        
        # Set game over
        self.game_state.set_game_over('white')
        self.assertTrue(self.game_state.is_game_over)
        self.assertEqual(self.game_state.winner, 'white')
    
    def test_both_kings_present(self):
        """Test that game continues when both kings are present."""
        self.assertFalse(self.board.is_king_captured('white'))
        self.assertFalse(self.board.is_king_captured('black'))
        
        # Make a move
        self.board.move_piece((1, 4), (3, 4))  # Move white pawn
        
        # Kings should still be present
        self.assertFalse(self.board.is_king_captured('white'))
        self.assertFalse(self.board.is_king_captured('black'))
    
    def test_win_after_king_capture(self):
        """Test complete win scenario."""
        # Simulate a capture of black king
        self.board.board[7][4] = None  # Remove black king
        
        # Check win condition
        if self.board.is_king_captured('black'):
            self.game_state.set_game_over('white')
        
        self.assertTrue(self.game_state.is_game_over)
        self.assertEqual(self.game_state.winner, 'white')


if __name__ == '__main__':
    unittest.main()
