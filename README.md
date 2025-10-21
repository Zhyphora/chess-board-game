# Console-Based Chess Game

A Python implementation of a console-based chess game with full chess rules validation and unit tests.

## Features

- ✅ Standard 8x8 chessboard with piece symbols (P, R, N, B, Q, K)
- ✅ Full chess piece movement validation
- ✅ Input handling for algebraic notation (e.g., `e2 e4`) and numeric format (e.g., `1,3 2,3`)
- ✅ King capture win condition
- ✅ Turn-based gameplay (White vs Black)
- ✅ Comprehensive unit tests

## Project Structure

```
chess-game/
│
├── src/
│   ├── main.py                  # Entry point
│   ├── game/
│   │   ├── chess_game.py        # Main game logic
│   │   └── game_state.py        # Game state management
│   ├── board/
│   │   ├── chess_board.py       # Board setup and operations
│   │   └── board_renderer.py    # Board display
│   ├── pieces/
│   │   ├── piece.py             # Base piece class
│   │   ├── pawn.py              # Pawn logic
│   │   ├── rook.py              # Rook logic
│   │   ├── knight.py            # Knight logic
│   │   ├── bishop.py            # Bishop logic
│   │   ├── queen.py             # Queen logic
│   │   └── king.py              # King logic
│   ├── moves/
│   │   ├── move_validator.py    # Move validation
│   │   └── move_generator.py    # Move generation
│   ├── input/
│   │   └── input_handler.py     # Input parsing
│   └── utils/
│       └── position.py          # Position utilities
│
├── tests/
│   ├── test_chess_board.py      # Board tests
│   ├── test_pieces.py           # Piece movement tests
│   ├── test_move_validator.py   # Move validation tests
│   └── test_game_state.py       # Game state tests
│
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8 or higher
- No external dependencies required (uses standard library only)

## Installation

### 1. Clone or download the repository

```bash
cd chess-game
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**On Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies (if any)

```bash
pip install -r requirements.txt
```

## How to Run

### Start the Game

```bash
python3 src/main.py
```

or

```bash
cd src
python3 main.py
```

### Run Unit Tests

**Run all tests:**

```bash
python3 -m unittest discover tests/
```

**Run specific test file:**

```bash
python3 -m unittest tests/test_chess_board.py
python3 -m unittest tests/test_pieces.py
python3 -m unittest tests/test_move_validator.py
python3 -m unittest tests/test_game_state.py
```

**Run with verbose output:**

```bash
python3 -m unittest discover tests/ -v
```

## How to Play

### Game Board

The game board is displayed with coordinates:

- **Columns**: a-h (left to right)
- **Rows**: 1-8 (bottom to top)

```
  a b c d e f g h
  ---------------
8|r n b q k b n r|8
7|p p p p p p p p|7
6|. . . . . . . .|6
5|. . . . . . . .|5
4|. . . . . . . .|4
3|. . . . . . . .|3
2|P P P P P P P P|2
1|R N B Q K B N R|1
  ---------------
  a b c d e f g h
```

### Piece Symbols

- **White pieces** (uppercase): `P` (Pawn), `R` (Rook), `N` (Knight), `B` (Bishop), `Q` (Queen), `K` (King)
- **Black pieces** (lowercase): `p` (Pawn), `r` (Rook), `n` (Knight), `b` (Bishop), `q` (Queen), `k` (King)

### Input Formats

You can enter moves in two formats:

**1. Algebraic notation (recommended):**

```
e2 e4    # Move piece from e2 to e4
b1 c3    # Move knight from b1 to c3
```

**2. Numeric format:**

```
1,3 2,3  # Move piece from row 1, col 3 to row 2, col 3
6,4 4,4  # Move piece from row 6, col 4 to row 4, col 4
```

**3. Alternative formats:**

```
e2,e4    # Algebraic with comma
1,3,2,3  # Numeric with comma separator
```

### Example Game Session

```
==================================================
     Welcome to Console Chess Game!
==================================================

How to play:
- Enter moves in format: 'e2 e4' (algebraic notation)
- Or use numeric format: '1,3 2,3'
- White pieces: P R N B Q K (uppercase)
- Black pieces: p r n b q k (lowercase)
- Game ends when a King is captured
- Type 'quit' to exit

  a b c d e f g h
  ---------------
8|r n b q k b n r|8
7|p p p p p p p p|7
6|. . . . . . . .|6
5|. . . . . . . .|5
4|. . . . . . . .|4
3|. . . . . . . .|3
2|P P P P P P P P|2
1|R N B Q K B N R|1
  ---------------
  a b c d e f g h

White's turn
Enter move (e.g., 'e2 e4' or '1,3 2,3'): e2 e4

Black's turn
Enter move (e.g., 'e2 e4' or '1,3 2,3'): e7 e5
```

### Game Rules Implemented

#### Pawn ♟️

- Moves forward one square
- Can move two squares forward from starting position
- Captures diagonally one square

#### Rook ♜

- Moves horizontally or vertically any number of squares
- Cannot jump over pieces

#### Knight ♞

- Moves in L-shape (2 squares in one direction, 1 in perpendicular)
- Can jump over other pieces

#### Bishop ♝

- Moves diagonally any number of squares
- Cannot jump over pieces

#### Queen ♛

- Combines rook and bishop movements
- Moves horizontally, vertically, or diagonally

#### King ♚

- Moves one square in any direction

### Win Condition

The game ends when a King is captured (simplified chess rules).

### Commands

- Type `quit`, `exit`, or `q` to exit the game at any time

## Validations Implemented

### Input Validation

- ✅ Validates input format (algebraic or numeric)
- ✅ Checks position boundaries (within 8x8 board)
- ✅ Handles invalid input gracefully with error messages

### Move Validation

- ✅ Ensures piece exists at starting position
- ✅ Validates piece belongs to current player
- ✅ Checks moves are legal for each piece type
- ✅ Prevents capturing own pieces
- ✅ Validates path is clear (except knights)

### Game Flow Validation

- ✅ Enforces turn-based gameplay
- ✅ Detects king capture
- ✅ Tracks move history
- ✅ Prevents illegal board modifications

## Unit Tests Coverage

### 1. Board Initialization Tests (`test_chess_board.py`)

- ✅ Test board is 8x8
- ✅ Test all pieces are in correct starting positions
- ✅ Test piece colors (uppercase = white, lowercase = black)
- ✅ Test empty squares

### 2. Piece Movement Tests (`test_pieces.py`)

- ✅ Test valid moves for each piece type
- ✅ Test invalid moves for each piece type
- ✅ Test piece-specific rules (e.g., knight L-shape, pawn diagonal capture)
- ✅ Test path blocking for rook, bishop, queen

### 3. Move Validation Tests (`test_move_validator.py`)

- ✅ Test boundary checking
- ✅ Test turn validation
- ✅ Test capturing rules
- ✅ Test invalid move detection

### 4. Win Condition Tests (`test_game_state.py`)

- ✅ Test king capture detection
- ✅ Test game over state
- ✅ Test winner determination
- ✅ Test move history tracking

### Running Tests

```bash
# Run all tests
python3 -m unittest discover tests/ -v

# Run specific test
python3 -m unittest tests.test_chess_board -v

# Run with coverage (if coverage installed)
pip install coverage
coverage run -m unittest discover tests/
coverage report
```

## Troubleshooting

### Issue: `ModuleNotFoundError`

**Solution**: Make sure you're in the project root directory and running:

```bash
python3 src/main.py
```

### Issue: Import errors in tests

**Solution**: Tests automatically add src to path, but ensure you run from project root:

```bash
python3 -m unittest discover tests/
```

### Issue: Virtual environment not activating

**Solution**:

- On macOS/Linux: `source venv/bin/activate`
- On Windows: `venv\Scripts\activate`
- Check Python version: `python3 --version`

## Deactivate Virtual Environment

When you're done:

```bash
deactivate
```

## Future Enhancements

- [ ] Check and checkmate detection
- [ ] Stalemate detection
- [ ] Castling move
- [ ] En passant capture
- [ ] Pawn promotion to queen
- [ ] Move notation history display
- [ ] Save/load game state
- [ ] Undo/redo moves
- [ ] AI opponent
- [ ] Time controls
- [ ] GUI interface

## Development

### Code Structure

- **Separation of Concerns**: Game logic, board management, and input handling are separate
- **OOP Design**: Each piece type inherits from base `Piece` class
- **Validation**: Multiple layers of validation for robust error handling
- **Testing**: Comprehensive unit tests for all components

### Adding New Features

1. **Add new piece type**: Create new class in `src/pieces/` inheriting from `Piece`
2. **Add new rule**: Modify validation logic in `src/board/chess_board.py`
3. **Add tests**: Create tests in `tests/` directory

## License

MIT License

## Author

GIThuberHenry

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## Contact

For questions or issues, please open an issue on GitHub

A Python implementation of a console-based chess game with full chess rules validation and unit tests.

## Features

- ✅ Standard 8x8 chessboard with piece symbols
- ✅ Full chess piece movement validation
- ✅ Input handling for algebraic notation (e.g., `e2 e4` or `e2,e4`)
- ✅ King capture win condition
- ✅ Turn-based gameplay (White vs Black)
- ✅ Comprehensive unit tests

## Project Structure

```
chess-game/
│
├── src/
│   ├── main.py                  # Entry point
│   ├── game/
│   │   ├── chess_game.py        # Main game logic
│   │   └── game_state.py        # Game state management
│   ├── board/
│   │   ├── chess_board.py       # Board setup and operations
│   │   └── board_renderer.py    # Board display
│   ├── pieces/
│   │   ├── piece.py             # Base piece class
│   │   ├── pawn.py              # Pawn logic
│   │   ├── rook.py              # Rook logic
│   │   ├── knight.py            # Knight logic
│   │   ├── bishop.py            # Bishop logic
│   │   ├── queen.py             # Queen logic
│   │   └── king.py              # King logic 
│   ├── input/
│   │   └── input_handler.py     # Input parsing
│   └── utils/
│       └── position.py          # Position utilities
│
├── tests/
│   ├── test_chess_board.py
│   ├── test_pieces.py
│   ├── test_move_validator.py
│   └── test_game_state.py
│
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8 or higher
- No external dependencies required (uses standard library only)

## Installation

1. **Clone or download the repository:**

```bash
cd chess-game
```

2. **Create a virtual environment:**

```bash
python3 -m venv venv
```

3. **Activate the virtual environment:**

   - On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies (if any):**

```bash
pip install -r requirements.txt
```

## How to Run

### Start the Game

```bash
python3 src/main.py
```

or

```bash
python3 -m src.main
```

### Run Unit Tests

Run all tests:

```bash
python3 -m pytest tests/
```

or using unittest:

```bash
python3 -m unittest discover tests/
```

Run specific test file:

```bash
python3 -m pytest tests/test_chess_board.py
```

## How to Play

1. The game starts with White's turn
2. The board is displayed with piece symbols:

   - **White pieces**: `P` (Pawn), `R` (Rook), `N` (Knight), `B` (Bishop), `Q` (Queen), `K` (King)
   - **Black pieces**: `p` (Pawn), `r` (Rook), `n` (Knight), `b` (Bishop), `q` (Queen), `k` (King)

3. **Input format**:

   - Algebraic notation: `e2 e4` (move piece from e2 to e4)
   - Alternative format: `e2,e4`
   - Numeric format: `1,4 3,4`

4. **Example moves**:

   ```
   White's move: e2 e4    # Move white pawn forward
   Black's move: e7 e5    # Move black pawn forward
   White's move: g1 f3    # Move white knight
   ```

5. The game ends when a King is captured

## Game Rules Implemented

- ♟️ **Pawn**: Moves forward one square (two on first move), captures diagonally
- ♜ **Rook**: Moves horizontally or vertically any number of squares
- ♞ **Knight**: Moves in L-shape (2+1 squares)
- ♝ **Bishop**: Moves diagonally any number of squares
- ♛ **Queen**: Combines rook and bishop movements
- ♚ **King**: Moves one square in any direction

## Validations

- Input format validation
- Boundary checking (moves within 8x8 board)
- Piece-specific move validation
- Turn validation (white/black alternating)
- Occupied square validation
- Path obstruction checking (except knights)

## Testing

The project includes comprehensive unit tests:

- ✅ Board initialization tests
- ✅ Valid/invalid move tests for all pieces
- ✅ Win condition tests (king capture)
- ✅ Input validation tests
- ✅ Game state tests

## Deactivate Virtual Environment

When you're done:

```bash
deactivate
```

## Troubleshooting

**Issue**: `ModuleNotFoundError`

- Solution: Make sure you're running from the project root and virtual environment is activated

**Issue**: Import errors

- Solution: Run with `python3 -m src.main` instead of `python3 src/main.py`

## Future Enhancements

- [ ] Check and checkmate detection
- [ ] Castling
- [ ] En passant
- [ ] Pawn promotion
- [ ] Move history
- [ ] Save/load game state
- [ ] AI opponent

## License

MIT License

## Author

Dhanuwardhan
# chess-board-game
