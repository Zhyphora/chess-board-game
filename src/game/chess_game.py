from board.chess_board import ChessBoard
from game.game_state import GameState
from input.input_handler import InputHandler


class ChessGame:
    """Main chess game controller."""
    
    def __init__(self):
        self.board = ChessBoard()
        self.game_state = GameState()
        self.input_handler = InputHandler()

    def start_game(self):
        """Start and run the chess game loop."""
        print("=" * 50)
        print("     Welcome to Console Chess Game!")
        print("=" * 50)
        print("\nHow to play:")
        print("- Enter moves in format: 'e2 e4' (algebraic notation)")
        print("- Or use numeric format: '1,3 2,3'")
        print("- White pieces: P R N B Q K (uppercase)")
        print("- Black pieces: p r n b q k (lowercase)")
        print("- Game ends when a King is captured")
        print("- Type 'quit' to exit\n")
        
        self.board.render()
        
        while not self.game_state.is_game_over:
            # Get current player
            current_player = self.game_state.current_player
            
            # Get move input
            move_input = self.input_handler.get_move_input(current_player)
            
            # Check for quit command
            if move_input.lower() in ['quit', 'exit', 'q']:
                print("\nGame terminated by player.")
                break
            
            # Parse move
            start, end = self.input_handler.parse_move(move_input)
            
            if start is None or end is None:
                print("❌ Invalid input format. Try 'e2 e4' or '1,3 2,3'\n")
                continue
            
            # Validate move
            is_valid, error_message = self.board.validate_move(start, end, current_player)
            
            if not is_valid:
                print(f"❌ {error_message}\n")
                continue
            
            # Execute move
            piece = self.board.get_piece(start)
            captured_piece = self.board.get_piece(end)
            self.board.move_piece(start, end)
            
            # Record move
            self.game_state.add_move(start, end, piece)
            
            # Display board
            self.board.render()
            
            # Show move feedback
            if captured_piece:
                print(f"✓ {current_player.capitalize()} captured {captured_piece}!")
            
            # Check for king capture (win condition)
            opponent = 'black' if current_player == 'white' else 'white'
            if self.board.is_king_captured(opponent):
                self.game_state.set_game_over(current_player)
                print("=" * 50)
                print(f"🎉 GAME OVER! {current_player.upper()} WINS!")
                print(f"    {opponent.capitalize()}'s King has been captured!")
                print("=" * 50)
                print(f"\nTotal moves: {len(self.game_state.move_history)}")
                break
            
            # Switch player
            self.game_state.switch_player()
            print()


def main():
    """Entry point for the chess game."""
    game = ChessGame()
    game.start_game()


if __name__ == "__main__":
    main()
