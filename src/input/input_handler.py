from utils.position import algebraic_to_index, parse_numeric_position, is_valid_position


class InputHandler:
    """Handles parsing and validation of user input."""
    
    @staticmethod
    def parse_move(move_input):
        """
        Parse move input in various formats.
        
        Supported formats:
        - Algebraic: "e2 e4" or "e2,e4"
        - Numeric: "1,3 2,3" or "1,3,2,3"
        
        Args:
            move_input: String containing the move
            
        Returns:
            Tuple (start_pos, end_pos) or (None, None) if invalid
        """
        move_input = move_input.strip().lower()
        
        # Try space separator first
        if ' ' in move_input:
            parts = move_input.split()
            if len(parts) == 2:
                return InputHandler._parse_positions(parts[0], parts[1])
        
        # Try comma separator with space: "e2,e4" or "1,3,2,3"
        if ',' in move_input:
            parts = move_input.split(',')
            
            # Format: "1,3,2,3" (4 parts)
            if len(parts) == 4:
                start = f"{parts[0]},{parts[1]}"
                end = f"{parts[2]},{parts[3]}"
                start_pos = parse_numeric_position(start)
                end_pos = parse_numeric_position(end)
                if start_pos and end_pos:
                    return start_pos, end_pos
            
            # Format: "e2,e4" (2 parts)
            elif len(parts) == 2:
                return InputHandler._parse_positions(parts[0], parts[1])
        
        return None, None

    @staticmethod
    def _parse_positions(start_str, end_str):
        """Parse individual position strings."""
        start_str = start_str.strip()
        end_str = end_str.strip()
        
        # Try algebraic notation (e.g., "e2")
        if is_valid_position(start_str) and is_valid_position(end_str):
            start_pos = algebraic_to_index(start_str)
            end_pos = algebraic_to_index(end_str)
            if start_pos and end_pos:
                return start_pos, end_pos
        
        # Try numeric notation (e.g., "1,3")
        if ',' in start_str and ',' in end_str:
            start_pos = parse_numeric_position(start_str)
            end_pos = parse_numeric_position(end_str)
            if start_pos and end_pos:
                return start_pos, end_pos
        
        return None, None

    @staticmethod
    def get_move_input(current_player):
        """
        Prompt user for move input.
        
        Args:
            current_player: 'white' or 'black'
            
        Returns:
            String containing user input
        """
        player_name = current_player.capitalize()
        print(f"{player_name}'s turn")
        move = input("Enter move (e.g., 'e2 e4' or '1,3 2,3'): ")
        return move
