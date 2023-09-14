# Set 4 Class - Libraries - Random library

import random # Imports all functions of "random" library
#from random import choice # Imports only "choice" function

# Hardcoded coin toss
# coin = random.choice(["heads","tails"])
# print(coin)

# Randint function
# number = random.randint(1,10)
# print(number)

# Shuffle function
cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)