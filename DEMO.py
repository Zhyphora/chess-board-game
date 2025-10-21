#!/usr/bin/env python3
"""
Demo script to show how to play the chess game.
This demonstrates a few sample moves.
"""

# Sample moves that can be used in the game:
sample_moves = """
SAMPLE CHESS GAME MOVES
========================

Opening moves (Black):
- e2 e4    (Move pawn from e2 to e4)
- d2 d4    (Move pawn from d2 to d4)
- g1 f3    (Move knight from g1 to f3)

Opening moves (White):
- e7 e5    (Move pawn from e7 to e5)
- d7 d5    (Move pawn from d7 to d5)
- b8 c6    (Move knight from b8 to c6)

Alternative notation (numeric):
- 1,4 3,4  (Same as e2 e4)
- 6,4 4,4  (Same as e7 e5)

Commands:
- quit     (Exit the game)
- exit     (Exit the game)
- q        (Exit the game)

EXAMPLE GAME SESSION
=====================

White's turn
Enter move: e2 e4

Black's turn
Enter move: e7 e5

White's turn
Enter move: g1 f3

Black's turn
Enter move: b8 c6

White's turn
Enter move: f1 c4

Black's turn
Enter move: f8 c5

... and so on until a king is captured!

TIPS
=====
1. The board shows coordinates on the sides
2. Uppercase letters = White pieces (P, R, N, B, Q, K)
3. Lowercase letters = Black pieces (p, r, n, b, q, k)
4. '.' represents an empty square
5. You must follow chess piece movement rules
6. You cannot capture your own pieces
7. Game ends when a King is captured (simplified rules)

PIECE MOVEMENTS
================
Pawn (P/p):
- Moves forward one square
- Can move two squares on first move
- Captures diagonally

Rook (R/r):
- Moves horizontally or vertically
- Any number of squares

Knight (N/n):
- Moves in L-shape (2+1 squares)
- Can jump over pieces

Bishop (B/b):
- Moves diagonally
- Any number of squares

Queen (Q/q):
- Combines Rook + Bishop movements
- Most powerful piece

King (K/k):
- Moves one square in any direction
- Protect at all costs!
"""

if __name__ == "__main__":
    print(sample_moves)
    print("\nTo play the actual game, run: python3 src/main.py")
