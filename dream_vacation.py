# 7-10. Dream Vacation: Write a program that polls users about their dream vaca­ tion. Write a prompt similar to If you could visit one place in the world, where  would you go? Include a block of code that prints the results of the poll. 

poll = {}

active = True

while active:
    name = input("What is your name? ")
    place = input("Where do you want to take your dream vacation? ")

    poll[name] = place
    
    print("Thank you for participating in our poll!")
    response = input('Would you want another person to answer this poll? (yes/no)')
    if response == 'no':
        active = False

print("--- Poll Results ---")

for name, place in poll.items():
    print(f"{name.title()} would like to go to {place.title()}.")