import random

grid_user = []
# Creating the grid
for i in range(10):
    row = []
    for j in range(10):
        row.append(".")
    grid_user.append(row)

for row in grid_user:
    print(" ".join(map(str, row)))

# Creating the grid for computer but without printing
grid_computer = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(".")
    grid_computer.append(row)

# User allocates their ships
def allocate_user_ships(grid_user, user_ships):
    print("Allocate ships for the user")

    for ship in range(5):
        # Loop enables check if allocation of the ships is valid and within the grid
        while True: 
            x = int(input("Enter the x coordinate of the ship: "))
            y = int(input("Enter the y coordinate of the ship: "))

            if (x, y) in user_ships:
                print("This coordinate is already taken. Please choose another one!")
            elif x < 0 or x > 9 or y < 0 or y > 9:
                print("Your coordinates are not valid. Please choose within the valid range of 0 to 9")
            else:
                grid_user[x][y] = "X"
                user_ships.append((x, y))
                break

    print("Updated grid after placing ship:")

    print(" ", " ".join(str(i) for i in range(len(grid_user))))
    for i, row in enumerate(grid_user):
        print(f"{i} {' '.join(str(cell) for cell in row)}")

# Random allocation of computer's ship 
def allocate_computer_ships(grid_computer, computer_ships):
    print("Ships of computer were allocated.")
    computer_ships = []
    for ship in range(5):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        grid_computer[x][y] = "X"
        computer_ships.append((x, y))
    # Following print is used to check if allocation happened correctly. To make computer's choice invisible, please outcomment the line below
    print(computer_ships)

# User takes a turn to shoot 
def user_turn(grid_computer, user_ships):
    print("User's turn to shoot!")
    print("Enter the coordinates of the cell you want to hit")

    # Check if user shoot within the valid range of grid
    while True:
        x = int(input("Enter the x coordinate: "))
        y = int(input("Enter the y coordinate: "))

        if x < 0 or x > 9 or y < 0 or y > 9:
            print("You are shooting outside of the grid. Try one more time")
        elif grid_computer[x][y] == "X":
            grid_computer[x][y] = "O"
            print("Hit!")
        else:
            print("Miss!")
            break

# Computer takes turn to shoot
def computer_turn(grid_user, computer_ships):
    print("Computer's turn to shoot!")
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    if grid_user[x][y] == "X":
        grid_user[x][y] = "O"                                            # shots of computer are displayed as "O", in case it hits user's ship
        print("Hit!")
        
        print(" ", " ".join(str(i) for i in range(len(grid_user))))
    for i, row in enumerate(grid_user):
        print(f"{i} {' '.join(str(cell) for cell in row)}")
    else:
        if grid_user[x][y] == ".":                                   
            grid_user[x][y] = "!"                                         # shots of computer are displayed as "!", in case it misses
            print("Miss!")
            print(" ", " ".join(str(i) for i in range(len(grid_user))))
    for i, row in enumerate(grid_user):
        print(f"{i} {' '.join(str(cell) for cell in row)}")

# Initiation of the full game until game_over condition is reached
def main():
    grid_user = [["." for _ in range(10)] for _ in range(10)]
    grid_computer = [["." for _ in range(10)] for _ in range(10)]
    user_ships = []
    computer_ships = []
    game_over = False

    allocate_user_ships(grid_user, user_ships)
    allocate_computer_ships(grid_computer, computer_ships)

    while not game_over:
        user_turn(grid_computer, user_ships)
        if all(cell == "O" for row in grid_computer for cell in row):
            game_over = True
            print("Game Over!")
            print("The user won!")
            break
        if all(cell != "X" for row in grid_user for cell in row):
            game_over = True
            print("Game Over!")
            print("Computer won!")
            break
        computer_turn(grid_user, computer_ships)
        if all(cell == "O" for row in grid_user for cell in row):
            game_over = True
            print("Game Over!")
            print("Computer won!")
            break
        if all(cell != "X" for row in grid_computer for cell in row):
            game_over = True
            print("Game Over!")
            print("The user won!")
            break

if __name__ == "__main__":
    main()
