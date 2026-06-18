# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make  two new dictionaries representing different people, and store all three dictionar­ ies in a list called people. Loop through your list of people. As you loop through  the list, print everything you know about each person. 

Benny = {'First name': 'Benson',
    'Last name': 'Trinidad',
    'age': 29,
    'city': 'Los Angeles'
    }

Mordecai = {'First name': 'Mordecai',
    'Last name': 'Regularshow',
    'age': 28,
    'city': 'California',
    }

Rigby = {'First name': 'Rigby',
    'Last name': 'Riggerson',
    'age': 28,
    'city': 'California',
    }

Skips = {'First name': 'Walks',
    'Last name': 'Quippenger',
    'age': 28,
    'city': 'California',
    }

people = [Benny, Mordecai, Rigby, Skips]

for person in people:
    print(f"{person['First name'].title()} {person['Last name'].title()}'s "
    "information:\n")

    for info in person.keys():
        if isinstance(person[info], int):
            print(f"\t{info.title()}: {person[info]}")
        else:
            print(f"\t{info.title()}: {person[info].title()}")
    print("\n")

