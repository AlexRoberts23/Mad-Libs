'''
Alex Roberts
This program asks the user for different types of words and creates a Mad Libs
story with them.
'''
name = input("What is your name? ")
print(f"Hello {name}!")
adj1 = input("Give an adjective: ")
per1 = input("Give the name of a person: ")
veh1 = input("Give a vehicle: ")
adj2 = input("Give another adjective: ")
adv1 = input("Give an adverb: ")
cre1 = input("Give a creature: ")
adj3 = input("Give another adjective: ")

print(f"\nIt was a {adj1} fall night.")
print(f"{per1} and I were excited to go to the pumpkin patch.")
print(f"We drove a {veh1} there and found the place {adj2}.")
print(f"We {adv1} picked our pumpkins and went to leave when all of a sudden—")
print(f"A {cre1} jumped in our path! How {adj3}!")