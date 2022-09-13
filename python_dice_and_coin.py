'''#Rhis is a comment 
this is a comment too
#Flip a coin program 
from random import choice, random 
#1st method use random.random()
#coin_flip_with_random = "head" if random()> 0.5 else "tails"
#2nd method
coin_flip_with_choice = choice(["japan", "mexico", "LA", "bubai", "australia", "new york", "stay home", "seattle", "mexico city", "the burmuda triangle"])
print (coin_flip_with_choice)'''
#Roll a dice
#1st import to your libaries 
from random import randint 
repeat = True
while repeat:
  print("You rolled", randint (1,6))
  print ("Do you want to try again?")
  repeat = ("y" or "yes") in input(). lower()
