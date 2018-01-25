import random
import time

""" This version of Dragon Quest  starts by building a class to play the game. """

# Game adapted from Invent With Python. Golden rings and idea of number of lives has been added.
# The code in this file is for python 2. (Not python 3 as used in the link).
# https://inventwithpython.com


class DragonQuest(object):
    # The first method that all classes should provide is the constructor.
    # The game stores the players and keeps track of whose turn it is.
    def __init__(self, the_list_of_players):
        self.players = the_list_of_players
        self.round = 0 # When the game starts, no one has played yet. It's round 0.
        self.game_over = False # Game ends, when this flag becomes True.


    def displayIntro(self):
        print 'PLAY DRAGON QUEST!\nYou are in a land full of dragons. In a mountain,'
        print 'are two caves. In one cave, the dragon is friendly'
        print 'and will share his treasure with whoever enters. The other dragon'
        print 'is greedy and hungry, and will eat any intruder on sight.'
        print 'First player to collect three golden rings wins.'
        print 'Player is eliminated if they lose all their lives.'

    def play(self):
        if self.round == 0:
            self.displayIntro()

        # If there are no active players, or a player has won, the game is over.
        if self.game_over:
            return # The game has ended. No more rounds.

        self.round += 1
        print "\nDRAGON QUEST: Round #%d" % self.round
        for player in self.players:
            if player.active: # If a player has been eliminated, they don't get to play again.
                player.play()  # In each round, each player gets a turn, until the game is over.
        self.play() # A recursive call to play the next round!


class Player(object):
    # Each player has a number of lives and a number of rings. They also have a name.
    # A future version might feature two players or one human player against the computer.
    def __init__(self, lives, rings, player_name, player_type):
        self.number_of_golden_rings = rings
        self.number_of_lives = lives
        self.name = player_name
        self.type = player_type  # The player type can be human or computer. True for computer.
        self.active = True  # A player will become inactive, if for example, they lose all their lives.

    def __init__(self, player_name):
        self.number_of_golden_rings = 0
        self.number_of_lives = 3
        self.name = player_name
        self.type = False  # The player type can be human or computer. True for computer.
                           # The default of False indicates a human player.
        self.active = True  # A player will become inactive, if for example, they lose all their lives.


    # Any player can choose a cave if it is their turn.
    # If the player is a computer, it chooses the cave randomly.
    # A human player must enter their choice at the keyboard.
    def chooseCave(self):
        cave = 0
        if self.type == True:  # Player is a computer and will choose the cave randomly.
            cave = random.randint(1, 2)
            time.sleep(2)

        else: # Player is a human, and will enter the cave of their choice at the terminal.
            while cave != 1 and cave != 2:
                print '%s, which cave will you go into? (1 or 2)' % self.name
                cave = input()
        print "%s has chosen cave #%d" % (self.name, cave)
        return cave


    def checkCave(self, chosenCave):
        print '%s approaches the cave...' % self.name
        time.sleep(2)
        print 'It is dark and spooky...'
        time.sleep(2)
        print 'A large dragon jumps out in front of %s! He opens his jaws and...' % self.name
        time.sleep(2)

        friendlyCave = random.randint(1, 2)  # Randomly assign which cave has the friendly dragon.

        if chosenCave == friendlyCave:
            print ('Gives %s a golden ring!' % self.name).upper()
            self.number_of_golden_rings += 1
        else:
            print ('Gobbles down %s in one bite!' % self.name).upper()
            self.number_of_lives -= 1

        lives = "lives"
        if self.number_of_lives==1:
            lives = "life"
        rings = "rings"
        if self.number_of_golden_rings==1:
            rings = "ring"
        print '\nUpdated Player Stats: %s has %d %s left' % (self.name, self.number_of_lives,lives),
        print 'and %d golden %s.\n' % (self.number_of_golden_rings, rings)
        time.sleep(6)


    def check_if_game_over(self):
        if self.number_of_golden_rings == 3:
            game.game_over = True  # We have a winner. The game is over!
            print "Player %s wins! They have collected all three rings of power!" % self.name

        if self.number_of_lives <= 0:
            print "Sorry, player %s is eliminated! All their lives have been used up.\nNo more turns for this player." % self.name
            self.active = False
            # The game will also end if there are no longer any active players. They will have all been eliminated.
            number_of_active_players = 0
            for player in game.players:
                if player.active:
                    number_of_active_players += 1
            if number_of_active_players == 0:
                game.game_over=True
                print "THERE WERE NO WINNERS!"


    def play(self):
        # A method so a player can play one round in the game, and update their game stats.
        print "* * * * * * * * * * * * * * * * * * * * * * "
        print "This turn is for %s." % self.name
        cave = self.chooseCave()
        self.checkCave(cave)
        self.check_if_game_over()


if __name__ == "__main__":
    player1 = Player("Agent Smith")  # <-- Change to your name.
    player1.type = True

    player2 = Player("LightningFast")
    player2.type = True  # Player 2 is a computer.

    player3 = Player("Wintermute")
    player3.type = True

    # Add the AI named "Wintermute" here as a third player.

    game = DragonQuest( [player1, player2] )  # All players must be inside this list of players.
    game.play()
