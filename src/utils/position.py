def algebraic_to_index(position):
    """Convert algebraic notation (e.g., 'e4') to board indices (row, col)."""
    if len(position) != 2:
        return None
    column = ord(position[0].lower()) - ord('a')
    try:
        row = 8 - int(position[1])
        if 0 <= row < 8 and 0 <= column < 8:
            return (row, column)
    except ValueError:
        return None
    return None

def index_to_algebraic(row, col):
    """Convert board indices (row, col) to algebraic notation (e.g., 'e4')."""
    if 0 <= row < 8 and 0 <= col < 8:
        column = chr(col + ord('a'))
        row_str = str(8 - row)
        return column + row_str
    return None

def is_valid_position(position):
    """Check if the given position is valid on the chessboard."""
    if len(position) != 2:
        return False
    column = position[0].lower()
    row = position[1]
    return column in 'abcdefgh' and row in '12345678'

def parse_numeric_position(pos_str):
    """Parse numeric position like '1,3' to (row, col)."""
    try:
        parts = pos_str.split(',')
        if len(parts) == 2:
            row = int(parts[0])
            col = int(parts[1])
            if 0 <= row < 8 and 0 <= col < 8:
                return (row, col)
    except ValueError:
        return None
    return None