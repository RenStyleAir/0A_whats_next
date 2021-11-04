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
answers = []
print(random_eight)
for i in range(len(random_eight) -1):
    if random_eight[i+1] > random_eight[i]:
        answers.append('higher')
    else: 
        answers.append('lower')

print(answers)


#  turn the 11 12 13 in to jack queen king
