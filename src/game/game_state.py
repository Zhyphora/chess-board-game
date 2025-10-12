class GameState:
    """Manages the state of the chess game."""
    
    def __init__(self):
        self.current_player = 'white'
        self._is_game_over = False
        self.winner = None
        self.move_history = []

    @property
    def is_game_over(self):
        """Property to check if game is over."""
        return self._is_game_over

    def switch_player(self):
        """Switch turn to the other player."""
        self.current_player = 'black' if self.current_player == 'white' else 'white'

    def set_game_over(self, winner):
        """Set the game as over with a winner."""
        self.winner = winner
        self._is_game_over = True

    def add_move(self, start, end, piece):
        """Add a move to the history."""
        self.move_history.append({
            'start': start,
            'end': end,
            'piece': piece,
            'player': self.current_player
        })

    def reset_game(self):
        """Reset the game state to initial values."""
        self.current_player = 'white'
        self._is_game_over = False
        self.winner = None
        self.move_history = []