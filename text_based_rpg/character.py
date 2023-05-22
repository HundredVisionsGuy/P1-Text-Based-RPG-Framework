""" Our Character Class

We're going to add a random algorithm for generating stats:
4 D6 (6-sided dice)
Drop the lowest number
Add the rest

Strategy #2: 
SET an empty list (to add each D6 roll)
REPEAT 4 times:
    add a random number between 1 and 6 to the list
SORT the list from low to high or high to low (using sort and/or reverse)
REMOVE the lowest number
"""
import random



class Character:
    # constructor
    def __init__(self, name):
        self.name = name

    # methods