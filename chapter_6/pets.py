# 6-8. Pets: Make several dictionaries, where each dictionary represents a differ­ ent pet. In each dictionary, include the kind of animal and the owner’s name.  Store these dictionaries in a list called pets. Next, loop through your list and as  you do, print everything you know about each pet. 

Misha = {'Name': 'Misha',
    'age': 8,
    'owner': 'Puyos Family'
    }

Night = {'Name': 'NightNight',
    'age': 1,
    'owner': 'Sally'
    }

Apple = {'Name': 'Apo',
    'age': 1,
    'owner': 'Puyos Family'
    }

pets = [Misha, Night, Apple]

for pet in pets:
    print(f"{pet['Name'].title()}'s information:\n")

    for info in pet.keys():
        if isinstance(pet[info], int):
            print(f"\t{info.title()}: {pet[info]}")
        else:
            print(f"\t{info.title()}: {pet[info].title()}")
    print("\n")

