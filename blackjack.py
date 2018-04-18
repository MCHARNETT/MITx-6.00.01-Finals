# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:40:30 2017

@author: harne
"""
#Blackjack
import random
class BlackJack:

    deck = {'A': 4, 'K': 4, 'Q': 4}
    def shuffleDeck(deck):
        #returns a randomly shuffled deck
        copDeck = deck.copy()
        new_deck = []
        m = 0
        while(len(copDeck) !=  len(new_deck)):
            m = random.randint(0, len(copDeck)-1)
            if copDeck.get(m) not in new_deck:
                new_deck.append(copDeck[m])
        return new_deck
    
    print(shuffleDeck(deck))
    
        