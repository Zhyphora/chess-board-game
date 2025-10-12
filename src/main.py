"""
Main entry point for the Console Chess Game.
Run this file to start the game.
"""

from game.chess_game import ChessGame


if __name__ == "__main__":
    game = ChessGame()
    game.start_game()