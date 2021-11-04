# Whats next! a game of chance and memory.
# Can you get 7 point? 
# by RenAir

# - setup + git hub
# - dek of 13 cards, select 8 
# - read the cards out (hide card)...

import random


deck = []
for card in range(13):
    deck.append(card +1)

random_eight = random.sample(deck, 8 )

print(random_eight)

#  turn the 11 12 13 in to jack queen king
