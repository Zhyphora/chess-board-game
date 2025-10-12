def render_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))

def display_chess_board(chess_board):
    rendered_board = []
    for row in chess_board:
        rendered_row = []
        for piece in row:
            if piece is None:
                rendered_row.append(" . ")
            else:
                rendered_row.append(f" {piece.symbol} ")
        rendered_board.append(rendered_row)
    render_board(rendered_board)