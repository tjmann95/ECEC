from Tkinter import *
import random

# Based on a project from Team Kraken (captain Adam Hoinkis) in Spring 2016
# Modified for a 3x4 Dragon Puzzle.


# Declare some global variables, which will be available anywhere.
global free_space
global prev_move;

free_space = 11
prev_move = 12
started = False
total_moves = 0
stack_of_moves = []  # Records the number of each tile that is moved and where it was placed. Each move is this a tuple.
                     # Can be used to "Solve" the puzzle by popping the entire stack in reverse.



# Function to start the game
def start():
    start_button.configure(state=DISABLED)
    canvas.delete(ALL)                                          # Remove original complete image

    shiftdown = canvas.winfo_y()                                # Shifts all the tiles down to make way for the info_frame at the top.
    for i, im in enumerate(tile_images):                        # Place each tile in a small canvas 250 * 200.
        tile = Canvas(puzzle_root, width=250, height=200)
        tile.create_image(0, 0, anchor=NW, image=im, tags=str(i))      # tag the tile with its original location 0 - 11.
        if i != 11: tile.place(x= (i % 4) * 250, y=(i/4) * 200 + shiftdown)        # Place in a 3x4 grid
        tiles.append(tile)
    tiles.append(0)                                             # 0 to represent the blank tile

    for tile in tiles:
        if tile != 0:
            tile.bind("<Button-1>", click_tile)                 # bind every tile to the mouse-click event
    status_label.configure(text="Status: Scrambling tiles")
    puzzle_root.after(2000, mix_up, 0)
    # Add code to enable the SOLVE button here. Change its state to NORMAL.
    solve_button.configure(state=NORMAL)

# Scrambles the tiles at the beginning of the game.
def mix_up(n):
    global prev_move
    global started  # Boolean flag that becomes True once the shuffled puzzle is ready.
    global free_space
    status_label.configure(text="Status: Scrambling tiles")
    if n < 6:                                                  # Makes 6 "random" moves
        t = random.choice(valid[free_space])                    # Choose a random movable tile. The free_space is the key.
        while t == prev_move:                                   # Prevent trivial moves (back-and-forth of one tile)
            t = random.choice(valid[free_space])
        prev_move = free_space                                  # The new free_space is now where the last tile used to be.
        print "Moving tile #", t
        stack_of_moves.append( (free_space, ' <-- ', t ) )
        print "Stack of all moves so far:", stack_of_moves
        move_tile(t, 0)                                         # move the selected tile
        puzzle_root.after(400, mix_up, n+1)                     # recursively call mix_up with a delay.
    else:
        started = True                                          # The game has begun! (click event is now active)
        status_label.configure(text="Status: Puzzle Challenge in Progress")


# Recursive method to move the specified tile with a simple animation
# Each tile must be moved a total of 200 pixels (up or down) and 250 pixels (left or right).
def move_tile(t, n):
    global free_space
    global dx
    global dy
    global animated_tile
    global total_moves
    # Only do these calculations the first time.
    if n == 0:
        if tiles[t] == 0: return  # Can't move the blank tile.
        direction = free_space - t
        print "The direction integer is: ", direction
        # Each tile can only move in one of four directions.
        number_of_columns = 4  # The dragon puzzle is 3 x 4.
        up, down, left, right = -number_of_columns, number_of_columns, -1, 1
        se = 5; nw = -5  # Added to help with the diagonal moves in the last problem.
        # Add code here to define sw and ne.
        sw = 1; ne = -1
        dx = 0;
        dy = 0
        if direction == up:         dy = -20
        if direction == down:       dy = +20
        if direction == left:       dx = -25
        if direction == right:      dx = +25
        if direction == se:         dx = +25; dy = +20  # Code for a possible diagonal move!
        # Add code here to define dx and dy for the other three diagonal motions.
        if direction == sw:         dx = -25; dy = +20
        if direction == ne:         dx = +25; dy = -20
        if direction == nw:         dx = -25; dy = -20

        animated_tile = tiles[t]
        tiles[free_space] = tiles[t]  # The empty space is now occupied by the selected tile
        tiles[t] = 0  # The empty space will soon be where the selected tile was.
        free_space = t  # Change index of the empty space

    # Move the animated tile on every iteration through the animation.
    if n < 10:
        x = animated_tile.winfo_x() + dx
        y = animated_tile.winfo_y() + dy
        animated_tile.place(x=x, y=y)
        puzzle_root.after(10, move_tile, t, n + 1)

    if n==10:   # OK, move completed. Update the number of moves and check if we won!
        if started:
            total_moves += 1
            show_number_of_moves_widget.delete(0, END)      # Update the number of moves
            show_number_of_moves_widget.insert(0, total_moves)
            if check_win():  win()     # Check if this move won the game



# Check if the tiles are in the correct order
def check_win():
    for i in range(11):                                     # check only the first 11 tiles/spots
        if tiles[i] == 0: return False                    # if the empty spot is encountered, the game is not over
        if i != int(tiles[i].gettags(ALL)[0]):              # tile's tag doesn't match its location it's the wrong order
            return False
        if i == 10:                                          # made it through all tiles means it's the correct order
            return True



# Actions for when the player wins the game
def win():
    global total_moves
    solve_button.configure(state=DISABLED)
    canvas.create_image(0, 0, image=dragon, anchor=NW)      # Show the finished image.
    status_label.configure(text="Status: YOU WON! The dragon will grant you one wish.")
    for tile in tiles:
        if tile != 0:   tile.unbind("<Button-1>")           # Unbind all the tiles.

    # Add code here to destroy all the small tiles, revealing the complete dragon image underneath.
    for tile in tiles:
        try:
            tile.destroy()
        except AttributeError:
            pass

# Event handler for mouse click
def click_tile(event):
    global freespace
    if not started:                                     # Tiles are still being randomized, clicking is disabled
        return

    for i in range(12):                                 # Unbind tiles while the event is being handled
        if tiles[i] != 0:
            tiles[i].unbind("<Button-1>")

    t = tiles.index(event.widget)                       # Tile index
    print "The index of the clicked tile is:", t
    if t in valid[free_space]:                          # Check if tile is valid (movable)
        print "Moving tile #", t
        stack_of_moves.append( (free_space, ' <-- ', t ) )
        move_tile(t, 0)

    for i in range(12):                                  # rebind the event
        if tiles[i] != 0:
            tiles[i].bind("<Button-1>", click_tile)


def solve():
    k = 0
    while stack_of_moves:  # True until the list is empty.
        undo_move = stack_of_moves.pop()
        print "Undoing this move:", undo_move
        tile_number = undo_move[0]

        puzzle_root.after( k*700, move_tile, tile_number, 0 )
        k = k + 1  # Just a counter for the # of moves made to solve using simple "reverse all moves" strategy.

        # Initialize some variables
tiles = []
# dictionary with valid moves depending on where the empty space is located
valid = {0: [1, 4] + [5],
         1: [0, 2, 5] + [4, 6],
         2: [1, 3, 6] + [5, 7],
         3: [2, 7] + [6],
         4: [0, 5, 8] + [1, 9],
         5: [1, 4, 6, 9] + [0, 2, 8, 10],
         6: [2, 5, 7, 10] + [1, 3, 9, 11],
         7: [3, 6, 11] + [2, 10],
         8: [4, 9] + [5],
         9: [5, 8, 10] + [4, 6],
         10: [6, 9, 11] + [5, 7],
         11: [7, 10] + [6]}




# Build the initial GUI showing the puzzle image and a start button.
puzzle_root = Tk()
puzzle_root.title("Dragon Puzzle Game!")
puzzle_root.geometry("%dx%d" % (1000, 640))

dragon = PhotoImage(file="dragon_puzzle_images/Dragon_ALL.gif")
tile_images = []  # A list to hold the 12 small tiles. Each rectangular is 250x200 pixels.
# The tile images  are labelled 1 - 12, but the list indices are 0 -  11.

for i in range(1,13):
    if i<10: tile_images.append(PhotoImage(file="dragon_puzzle_images/Dragon-0%d.gif" % i))
    else:    tile_images.append(PhotoImage(file="dragon_puzzle_images/Dragon-%d.gif" % i))


info_frame = Frame(puzzle_root, bg="black")
info_frame.grid(row=0, sticky=EW)

canvas = Canvas(puzzle_root, width=1000, height=600, bg="black", bd=4)
canvas.create_image(0, 0, image=dragon, anchor=NW)
canvas.grid(row=1)

start_button = Button(info_frame, text="START", command=start, height=2)
# start_button.place(x=500, y=300)
start_button.grid(row=0, column=0)

solve_button = Button(info_frame, text="SOLVE", command=solve, height=2)
solve_button.grid(row=0, column=1)
# Add code to disable the SOLVE button here. Change its state to DISABLED.
solve_button.configure(state=DISABLED)

Label(info_frame, text="Number of Moves", bg="black", fg="green").grid(row=0, column=2)
show_number_of_moves_widget = Entry(info_frame, width=5, justify=CENTER)  # Add code to CENTER the display here.
show_number_of_moves_widget.delete(0, END)
show_number_of_moves_widget.insert(0, "0")
show_number_of_moves_widget.grid(row=0, column=3)

# Add code to display 0 here. Use the delete and then the insert command.
# Don't forget they each take two arguments.



status_label = Label(info_frame, text="Status: Press the Start button to begin!", bg="black", fg="green")
status_label.grid(row=0, column=4)

puzzle_root.mainloop()