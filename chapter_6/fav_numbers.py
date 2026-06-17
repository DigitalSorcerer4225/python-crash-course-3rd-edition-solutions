# Favorite Numbers: Use a dictionary to store people’s favorite numbers.  Think of five names, and use them as keys in your dictionary. Think of a favorite  
# number for each person, and store each as a value in your dictionary. Print  each person’s name and their favorite number.

favorite_numbers = {'dante': 777, 'mica': 62,
    'alice': 14, 'benson': 99, 'pinky': 3
    }

for person, number in favorite_numbers.items():
    print(f"{person.title()}'s favorite number is: {number}.")