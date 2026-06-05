# What are slice in the context of a list? How are they useful?
# What situations in which slicing through a subset of a list is useful?
# What are the ways of copying a list other than slicing through it?

#Slicing through a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#Looping through a slice

print("Here are the first three players on my team:")
for player in players[:3]:
    print(f"\t {player.title()}")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

friend_foods.append('hotdogs')
my_foods.append('tortillas')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)