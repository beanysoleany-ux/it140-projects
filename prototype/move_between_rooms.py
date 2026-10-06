"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# TODO: Set the player's starting room for the simplified prototype.
current_room = "Great Hall"

# TODO: Create the gameplay loop required by the milestone.
while True:
    # 1. Display the current room.
    print(f"\nYou are in the {current_room}.")

    # 2. Prompt for a movement command or "exit".
    command = input("Enter a move (north, south, east, west) or 'exit': ").strip().lower()

    # Handle the exit condition
    if command == "exit":
        print("Thanks for playing!")
        break

    # 3. Branch for a valid move, exit, or invalid input.
    # Check if the direction exists in the current room's dictionary
    if command in rooms[current_room]:
        # 4. Update the room only after a valid movement command.
        current_room = rooms[current_room][command]
    else:
        # Handle invalid directions or typos
        print("You can't go that way!")

    # 5. Continue until the required exit condition is reached.
