
# coding: utf-8

# In[3]:

import random


# In[63]:

def riffle(deck):
    first_half = []
    second_half = []
    
    i = 0
    while len(deck) > 0:
        if len(deck) == 1:
            if (i % 2 == 0):
                first_half += deck
                deck = []
            else:
                second_half += deck
                deck = []
        else:
            random_number_to_pick = random.randrange(1, len(deck),1)
            if (i % 2 == 0):
                first_half += deck[:random_number_to_pick]
                deck = deck[random_number_to_pick:]
            else:
                second_half += deck[:random_number_to_pick]
                deck = deck[random_number_to_pick:]
            i += 1

            
    new_deck = first_half + second_half
    
    return new_deck
        
    
def has_been_riffle_shuffled_once_only(deck):
    decks = [[],[]]
    i = 0
    a_or_b = 0
    current_number = 0
    
    while i < len(deck) - 1:
        if deck[i] > current_number:
            current_number = deck[i]
            decks[a_or_b % 2].append(current_number)
        else:
            current_number = deck[i]
            a_or_b += 1
            decks[a_or_b % 2].append(current_number)
        
        
        i += 1
    
    # Return false if decks are in original state
    if (decks[0] + decks[1] == sorted(decks[0] + decks[1])):
        return False
    
    # Return true when each half of a deck is sorted in increasing order
    elif (decks[0] == sorted(decks[0]) and decks[1] == sorted(decks[1])):
        return True
    
    # Otherwise return false (if each half is not sorted the deck must 
    # have been shuffled more than once)
    else:
        return False
        
            
        


# In[64]:

deck_of_cards = range(1,53)
new_deck_of_cards = riffle(deck_of_cards)
second_shuffle = riffle(new_deck_of_cards)


# In[65]:

print has_been_riffle_shuffled_once_only(deck_of_cards)
print has_been_riffle_shuffled_once_only(new_deck_of_cards)
print has_been_riffle_shuffled_once_only(second_shuffle)


# In[ ]:



