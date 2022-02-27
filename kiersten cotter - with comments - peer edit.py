# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Kiersten Cotter (with comments)
# Creation Date: 02-17-2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
#1-For consistancy - all text in the opening paragraph should line up along left side when the program is ran.
	print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
#2-The correct way to enter a blank line after text is show in /n. If you want more than one blank line you add more.
	n/:

def chooseCave():
        cave = ''
#2-Indent the while loop and line it up with cave. A while loop is the main body program.
        while cave != '1' and cave != '2':
                print('Which cave will you go into? (1 or 2)')
                cave = input()
#3-Indent return because the return is part of the while loop.
#4- 'caves' needs to be 'cave' - continuity 
        return 'caves'

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
#5-change the (3) below to a (2) for only 2 second of sleep.
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
#6-choosecave() needs to be chooseCave(). with two words in the saying the second word needs to be capitalized.
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
#7-planing needs to say playing. Grammer error.
		print("Thanks for playing")

