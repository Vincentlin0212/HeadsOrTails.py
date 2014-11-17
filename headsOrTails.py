#! /usr/bin/env python
import random
from special_input import *
print("Coin Guessing Game.")

life = 1
score = 0

while life >= 1:
	coin = random.choice(["heads", "tails"])
#	print("{}".format(coin)) # to have fun... ...
	guess = raw_input("Predict heads or tails >")
	if guess[0].lower() == coin[0]:
		score += 1
		print("It is {}.  Your score is: {}".format(coin, score))
	if guess == "IWTGML":
		print("Would you like more lifes?")
		magic = raw_input("Predict heads or tails >")
		if magic[0].lower() == coin[0]:
			moreLife = random.randint(1, 100)
			life += moreLife
			print("{} lifes have add to you.".format(moreLife))
		else:
			print("Bad luck")
			continue
	elif guess[0].lower() != coin[0]:
		life -= 1
		print("It is {}. Life -1!".format(coin))
		
print("You died, better luck next time.")
print("Your total scors is {}".format(score))

f = open("score.txt", "r+")
fileContents = int(f.read())
if score >= fileContents:
	f.seek(0)
	f.write(str(score))
	print("New high score: {}".format(score))
else:
	print("High score: {}".format(fileContents))
	
f.close()