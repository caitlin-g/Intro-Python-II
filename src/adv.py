from room import Room
from player import Player
from item import Item

# Nested lists of item names and ddescriptions
item_descriptions = [
    ['latern','light source'],
    ['machete','Use for protection'],
    ['gold','It\'s gold. Enough said']
]

items = [Item(item[0], item[1]) for item in item_descriptions]

print(items)

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player('Rupert', room['outside'])
print("Welcome, friend!")
print(input("Which direction would you like to move?: [n] North    [e] East    [s]    South    [w]West    [q] Quit\n"))
directions = ['n', 'e', 's', 'w', 'q']

# Function that will return the current room if the player moves 
# in an invalid direction
def move_rooms(direction, current_room):
    room_link = direction + '_to'
# Checks to see if we can move in that direction
    if hasattr(current_room, room_link):
# If true, we get the new room
        return getattr(current_room, room_link)
    else:
        print("Nothing that way! Try another direction")
        return current_room

# Write a loop that:
while not directions == 'q':
# * Prints the current room name
    print(new_player.current_room)
# * Prints the current description (the textwrap module might be useful here).
    print(new_player.current_room.description)

# * Waits for user input and decides what to do.
    direction = input("Where to next? [n] North    [e] East    [s]    South    [w]West    [q] Quit\n")

# If the user enters a cardinal direction, attempt to move to the room there.
# Uses the move_rooms function to determine the player's n ew current room
# based on the direction they input
    new_player.current_room = move_rooms(direction, new_player.current_room)

# If the user enters "q", quit the game.
    if direction == 'q':
        print("Thanks for playing!")
        break