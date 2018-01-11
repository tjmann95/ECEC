from Tkinter import *
import random

# Created by Team Kraken (captain Adam Hoinkis) in Spring 2016

# Function to start the game
def start():
    start_button.destroy()                                      # Destroy the start button
    canvas.delete(ALL)                                          # Remove original image

    for i, im in enumerate(tile_images):                        # Create 8 tiles from images
        tile = Canvas(puzzle_root, width=200, height=200)
        tile.create_image(100, 100, image=im, tags=str(i))      # tag the tile with its correct location
        tile.place(x= (i % 3) * 200, y=(i/3) * 200)             # Place in a 3x3 grid
        tiles.append(tile)
    tiles.append(0)                                             # 0 to represent the blank tile

    for i in range(8):                                          # bind every tile to the mouse-click event
        tiles[i].bind("<Button-1>", click_tile)
    mix_up(0)                                                   # Randomize the tiles


# Randomizes the tiles at the beginning of the game.
def mix_up(n):
    # global valid  # A dictionary with the allowed moves.
    global prev_move
    global started  # Boolean flag that becomes True once the shuffled puzzle is ready.

    if n < 6:                                                   # Makes 6 "random" moves
        t = random.choice(valid[free_space])                    # Choose a random movable tile. The free_space is the key.
        while t == prev_move:                                   # Prevent trivial moves (back-and-forth of one tile)
            t = random.choice(valid[free_space])
        prev_move = free_space                                  # The new free_space is now where the last tile used to be.
        print "Moving tile #", t

        puzzle_root.after(100, move_tile, t, 0)                 # move the selected tile
        puzzle_root.after(700, mix_up, n+1)                     # recursively call mix_up with a delay.
    else:
        started = True                                          # The game has begun! (click event is now active)


# recursive method to move the specified tile with a simple animation
# Each tile must be moved a total of 200 pixels in one of the four allowed directions.
def move_tile(t, n):
    if tiles[t]==0: return # Can't move the blank tile.
    global free_space
    if n < 20:                                              # 20 small increments in animation
        diff = free_space - t                               # diff determines which way to move the tile
        if diff < 0:
            if diff % 3 == 0:                               # -3 means move up
                x = tiles[t].winfo_x()
                y = tiles[t].winfo_y() - 10
            else:                                           # -1 means move left
                x = tiles[t].winfo_x() - 10
                y = tiles[t].winfo_y()
        else:
            if diff % 3 == 0:                               # 3 means move down
                x = tiles[t].winfo_x()
                y = tiles[t].winfo_y() + 10
            else:                                           # 1 means move right
                x = tiles[t].winfo_x() + 10
                y = tiles[t].winfo_y()

        tiles[t].place(x=x, y=y)
        puzzle_root.after(5, move_tile, t, n+1)
    else:
        #blank = tiles[free_space]
        tiles[free_space] = tiles[t]                        # The empty space is now occupied by the selected tile
        tiles[t] = 0                                        # The empty space is now where the selected tile was
        free_space = t                                      # Change index of the empty space
        if started:
            global total_moves
            total_moves += 1
            if check_win():                                 # Check if this move won the game
                win()

# Check if the tiles are in the correct order
def check_win():
    for i in range(8):                                      # check only the first 8 tiles/spots
        if tiles[i] == 0:                                   # if the empty spot is encountered, the game is not over
            return False
        if i != int(tiles[i].gettags(ALL)[0]):              # tile's tag doesn't match its location it's the wrong order
           return False
        if i == 7:                                          # made it through all 8 tiles means it's the correct order
            return True


# Actions for when the player wins the game
def win():
    global total_moves

    for i in range(8):                                      # Unbind everything
        tiles[i].unbind("<Button-1>")

    # Coordinates for Label to display score.
    if total_moves >= 100:                                  # three-digit numbers are longer
        x = 210
    else:
        x = 225

    winLabel = Label(puzzle_root, text="YOU WIN\nTotal Moves: %d" % total_moves, highlightbackground="black",
                         highlightthickness=2, bg="light gray", font="Ubuntu 16")
    winLabel.place(x=x, y=250)
    score = max((100 - total_moves), 0)  # You lose 1 point for each move. But score cannot be negative.



# Event handler for mouse click
def click_tile(event):
    if not started:                                     # Tiles are still being randomized, clicking is disabled
        return

    for i in range(9):                                  # Unbind tiles while the event is being handled
        if tiles[i] != 0:
            tiles[i].unbind("<Button-1>")

    t = tiles.index(event.widget)                       # Tile index
    if t in valid[free_space]:                          # Check if tile is valid (movable)
        move_tile(t, 0)

    for i in range(9):                                  # rebind the event
        if tiles[i] != 0:
            tiles[i].bind("<Button-1>", click_tile)


def solve():
    pass

# Initialize some variables
tiles = []
# dictionary with valid moves depending on where the empty space is located
valid = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4, 6], 4: [1, 3, 5, 7],
         5: [2, 4, 8], 6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}
free_space = 8
prev_move = 9
started = False
total_moves = 0

# Build the initial GUI showing the puzzle image and a start button.
puzzle_root = Tk()
puzzle_root.title("Puzzle Game - Unleash the Kraken!")
puzzle_root.geometry("%dx%d" % (600, 640))

kraken = PhotoImage(file="images/Puzzle/kraken_puzzle.gif")
tile_images = []  # A list to hold the 8 small tiles. Each is 200x200 pixels.
for i in range(1,9):
    tile_images.append(PhotoImage(file="images/Puzzle/kraken_0%d.gif" % i))

canvas = Canvas(puzzle_root, width=600, height=600, bg="seagreen")
canvas.create_image(300, 362, image=kraken, anchor=CENTER)
canvas.pack()

start_button = Button(puzzle_root, text="START", command=start)
start_button.place(x=268, y=300)

solve_button = Button(puzzle_root, text="SOLVE", command=solve)
solve_button.pack()

puzzle_root.mainloop()