from Tkinter import *

'''
Play Tic-Tac-Toe!
GUI uses a Tkinter canvas and mouse responses.
Two Player Version - so no computer logic needs to be implemented.
'''


"""
A Canvas has two components which affect the edges: the border (borderwidth attribute) and highlight ring (highlightthickness attribute).
If you have a border width of zero and a highlight thickness of zero, the canvas coordinates will begin at 0,0.
Otherwise, these two components of the canvas infringe upon the coordinate space.
What I most often do is set these attributes to zero.
Then, if I actually want a border I'll put that canvas inside a frame and give the frame a border."""


class TicTacToeGame:

    def __init__(self, master):
        # master frame
        self.frame = Frame(master,  padx=10, pady=10, background='bisque')
        self.frame.pack(side='top', fill="both", expand=True)

        # Canvas to display the nine squares
        self.canvas_for_board = Canvas(self.frame, width=300, height=300, background='blue', highlightthickness=0, bd=0)
        self.canvas_for_board.grid(row=0, column=0, columnspan=2, sticky="N")

        # Shows status of game and displays various messages.
        self.label_for_messages=Label(self.frame, text='Press button to start playing!', height=2, width=32,  bg='coral', fg='blue')
        self.label_for_messages.grid(row=1, column=0, columnspan=2, sticky=NSEW)

        self.x_label = Label(self.frame, bg='bisque', text="Score for X:")
        self.x_label.grid(row=2, column=0)

        self.score_for_x = Label(self.frame,  bg='blue', fg='white', justify=CENTER, width=5, text="0")
        self.score_for_x.grid(row=2, column=1)

        self.o_label = Label(self.frame, bg='bisque', text="Score for O:")
        self.o_label.grid(row=3, column=0)

        self.score_for_o = Label(self.frame,  bg='blue', fg='white', justify=CENTER, width=5, text="0")
        self.score_for_o.grid(row=3, column=1)


        # frame to contain the buttons
        self.frameb=Frame(self.frame, background = 'bisque')
        self.frameb.grid(row=4, column=0, columnspan=2, sticky=NSEW)

        # Buttons to initiate the game
        self.Start1=Button(self.frameb, text='START', command=self.start_for_2players_no_computer)
        self.Start1.pack()

        # self.Start2=Button(self.frameb, text='1 Player vs Computer', command=self.start2, bg='purple', fg='white')
        # self.Start2.pack(fill="both", expand=True, side=LEFT)
        # self.Start2=Button(self.frameb, text='1 Player vs Computer', command=self.start2, bg='purple', fg='white', state=DISABLED)
        # self.Start2.pack(side=LEFT)

        self.turn_number = 0
        self.TTT = [[]]
        self.game_number = 0


        self.game_number_label = Label(self.frame, text="Game Number", bg='bisque')
        self.game_number_label.grid(row=5, column=0)
        self.game_number_display = Label(self.frame, text="0", bg='bisque')
        self.game_number_display.grid(row=5, column=1)

        self.first_player_label = Label(self.frame, text="First Player", bg='bisque')
        self.first_player_label.grid(row=6, column=0)
        self.first_player_display = Label(self.frame, text="X", bg='bisque')
        self.first_player_display.grid(row=6, column=1)

        # canvas board drawing function call
        self.draw_board()

    def start_for_2players_no_computer(self):
        self.game_number += 1
        print "Restart new game for two players and no computer."
        self.game_number_display["text"] = self.game_number

        if (self.game_number % 2) == 1 :
            first_player = 'X'
        else:
            first_player = 'O'
        self.first_player_display.config(text = first_player)

        # refresh canvas
        self.canvas_for_board.delete(ALL)
        self.label_for_messages['text']=('Tic Tac Toe Game')

        # function call on click
        self.canvas_for_board.bind("<ButtonPress-1>", self.play)
        self.draw_board()

        # Initialize the TTT matrix. TTT = Tic-Tac-Toe, of course!
        # Stores the locations of the circles and crosses.
        # self.TTT = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.TTT = [ ['_', '_', '_'],  ['_', '_', '_'], ['_', '_', '_'] ]
        # Counter for the turn number should be 1 for the first turn.
        self.turn_number = 1

        # trigger to end game
        self.j = False
        self.Start1.config(text="NEW GAME")


    def end(self):
        # Ends the game
        self.canvas_for_board.unbind("<ButtonPress-1>")
        self.j = True

    # Draws a board of nine squares on the canvas, and encloses it all in a blue rectangle.
    def draw_board(self):
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                x = i*100
                y = j*100
                if (i+j) % 2 == 0:
                    self.canvas_for_board.create_rectangle(x, y, x+100, y+100, fill='ivory', outline='blue')
                else:
                    self.canvas_for_board.create_rectangle(x, y, x+100, y+100, fill='bisque', outline='blue')
        self.canvas_for_board.create_rectangle(0, 0, 300, 300,  outline='blue', width=6)

    #  I added this to use the "in" operator as a quick way to check for a winner.
    # First we create a new board holding Xs and Os.
    # Then we create a list, with the eight winning patterns 'XXX' and 'OOO'
    def check_for_winning_combos(self):
        # TTT is the board showing Xs and Os. Unoccupied squares shown with a '_'.
        b = [ ['_', '_', '_'],  ['_', '_', '_'], ['_', '_', '_'] ]
        # Winning patterns.
        for index1 in range(0, 3):
            for index2 in range(0, 3):
                if self.TTT[index1][index2] == 9:
                    b[index1][index2] = 'X'  # Board holds an 'X'
                elif self.TTT[index1][index2] == 1:
                    b[index1][index2] = 'O'  # Board holds an 'O' (Oh)

        print b
        r1 = self.TTT[0][0] + self.TTT[0][1] + self.TTT[0][2]
        r2 = self.TTT[1][0] + self.TTT[1][1] + self.TTT[1][2]
        r3 = self.TTT[2][0] + self.TTT[2][1] + self.TTT[2][2]
        c1 = self.TTT[0][0] + self.TTT[1][0] + self.TTT[2][0]
        c2 = self.TTT[0][1] + self.TTT[1][1] + self.TTT[2][1]
        c3 = self.TTT[0][2] + self.TTT[1][2] + self.TTT[2][2]
        d1 = self.TTT[0][0] + self.TTT[1][1] + self.TTT[2][2]
        d2 = self.TTT[2][0] + self.TTT[1][1] + self.TTT[0][2]
        wins = [r1, r2, r3, c1, c2, c3, d1, d2]
        print wins
        if 'XXX' in wins:
            message = "Player X wins!"
            print message
            self.label_for_messages['text'] = message
            newscore = int(self.score_for_x["text"] ) + 1
            self.score_for_x["text"] = str(newscore)
            print "Score for player X is now:", self.score_for_x["text"]
            change_color(self.label_for_messages, 8)

            self.end()
        elif 'OOO' in wins:
            message =  "Player O wins!"
            print message
            self.label_for_messages['text'] = message
            newscore = int(self.score_for_o["text"] ) + 1
            self.score_for_o["text"] = str(newscore)
            print "Score for player O is now:", self.score_for_o["text"]
            change_color(self.label_for_messages, 8)

            self.end()
        elif self.turn_number == 10:
            message = "No winner. It's a draw."
            print message
            self.label_for_messages['text'] = message
            change_color(self.label_for_messages, 8)
            self.end()

    def play(self, event):
        # Double player game loop. Player X versus Player O, - both human.
        for k in range(0, 300, 100):
            for j in range(0, 300, 100):
                # checks if the mouse input is in one of the nine squares.
                if event.x in range(k, k+100) and event.y in range(j, j+100):
                    print "Mouse click at:", (event.x, event.y)
                    # Checks the square is empty. Can't play the same square twice!
                    if self.canvas_for_board.find_enclosed(k, j, k+100, j+100) == ():
                        # Player X plays on the odd-numbered turns in odd numbered games. First turn is #1, (not 0).
                        if (self.turn_number + self.game_number) % 2 == 0:
                            # Places an X on the indicated square.
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            # self.canvas_for_board.create_oval( X+25, Y+25, X-25, Y-25, width=4, outline="black")
                            self.canvas_for_board.create_image(X, Y, image=x_image)
                            # self.TTT[Y1][X1] += 9
                            self.TTT[Y1][X1] = 'X'
                            self.turn_number += 1

                        # Player O plays on the even-numbered turns in odd-numbered games.
                        else:
                            # Places an O on the indicated square.
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            self.canvas_for_board.create_image(X, Y, image=o_image)
                            # self.TTT[Y1][X1] += 1
                            self.TTT[Y1][X1] = 'O'
                            self.turn_number += 1
        # Check to see if there is a winner.
        self.check_for_winning_combos()


# FLashes the widget n times. (i.e. 2n half flashes)
def change_color(my_widget, n):
    if n == 0:
        my_widget.config(background='coral')
        return
    else:
        current_color = my_widget.cget("background")
        next_color = "red" if current_color == "yellow" else "yellow"
        my_widget.config(background=next_color)
        root.after(250, change_color, my_widget , n-1)

# initiate the class
root = Tk()
root.title("TIC-TAC-TOE")
x_image = PhotoImage(file="images/X.gif")
o_image = PhotoImage(file="images/O.gif")

app = TicTacToeGame(root)

root.mainloop()
