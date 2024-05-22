# Battleship Game

Welcome to the Battleship game! This is a simple console-based implementation of the classic Battleship game where you can play against the computer.

## How to Play

### Setup

1. **Grid Initialization**: 
   - Two 10x10 grids are created: one for the user and one for the computer.
   - Grids are initially filled with "." to indicate empty cells.

2. **Ship Allocation**: 
   - The user is prompted to allocate their 5 ships by entering coordinates.
   - Ships are marked with "X" on the grid.
   - The computer randomly allocates its 5 ships on its grid (coordinates are not shown to the user).

### Gameplay

1. **User's Turn**:
   - The user is prompted to enter the coordinates to shoot at the computer's grid.
   - If the shot hits a ship, it is marked with "O".
   - If the shot misses, it is marked with "!".

2. **Computer's Turn**:
   - The computer randomly selects coordinates to shoot at the user's grid.
   - If the shot hits a ship, it is marked with "O".
   - If the shot misses, it is marked with "!".

### Winning Condition

- The game continues in turns until all ships of either the user or the computer are hit.
- The game ends and announces the winner when all ships on one grid are hit.

## Functions

- `allocate_user_ships(grid_user, user_ships)`: Allows the user to place their ships on the grid.
- `allocate_computer_ships(grid_computer, computer_ships)`: Randomly allocates the computer's ships on the grid.
- `user_turn(grid_computer, user_ships)`: Handles the user's turn to shoot.
- `computer_turn(grid_user, computer_ships)`: Handles the computer's turn to shoot.
- `main()`: The main function to initiate and control the game flow.

## Usage

1. Run the game by executing the script in a Python environment:
   ```bash
   python battleship.py
