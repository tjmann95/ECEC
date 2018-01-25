import random
import time


# Game adapted from Invent With Python. Golden rings and idea of number of lives has been added.
# The code in this file is for python 2. (Not python 3 as used in the link).
# https://inventwithpython.com

def displayIntro():
    print 'PLAY DRAGON QUEST!\nYou are in a land full of dragons. In front of you,'
    print 'you see two caves. In one cave, the dragon is friendly'
    print 'and will share his treasure with you. The other dragon'
    print 'is greedy and hungry, and will eat you on sight.'
    print 'Game ends when you win three golden rings, or run out of lives!'
    print 'STATUS: You have %d lives left.' % number_of_lives,
    print 'You have %d golden rings.\n' % number_of_golden_rings


def check_if_game_over():
    if number_of_lives == 0:
        print 'Sorry, you lose! All your lives have been used up. Try again after your next reincarnation!'
        return True
    if number_of_golden_rings == 3:
        print 'You win! Use your three rings of power wisely!'
        return True


def chooseCave():
    global turn_number
    turn_number += 1
    print 'Turn #', turn_number

    cave = ''
    # while cave != '1' and cave != '2':
    while cave != 1 and cave != 2:
        print 'Which cave will you go into? (1 or 2)'
        cave = input()
        print "You chose cave #", cave
    return cave


def checkCave(chosenCave):
    global number_of_lives
    global number_of_golden_rings

    print 'You approach the cave...'
    time.sleep(2)
    print 'It is dark and spooky...'
    time.sleep(2)
    print 'A large dragon jumps out in front of you! He opens his jaws and...'
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == friendlyCave:
        print 'Gives you a golden ring!'.upper()
        number_of_golden_rings += 1
    else:
        print 'Gobbles you down in one bite!'.upper()
        number_of_lives -= 1

    lives = "lives"
    rings = "rings"

    # Use two if statements here to handle the singular case.
    print '\nSTATUS: You have %d %s left.' % (number_of_lives, 'life' if number_of_lives == 1 else lives)
    print 'You have %d golden %s.\n' % (number_of_golden_rings, rings[0:4] if number_of_golden_rings == 1 else rings)

playAgain = 'yes'
number_of_lives = 3  # Game will end when all your lives are used up, or you accumulate three golden rings.
number_of_golden_rings = 0
turn_number = 0
game_over = False

while (playAgain == 'yes') or (playAgain == 'y'):

    if turn_number == 0:
        displayIntro()

    caveNumber = chooseCave()
    checkCave(caveNumber)

    if check_if_game_over():
        break

    print('Do you want to play again? (yes or no)')
    playAgain = raw_input()