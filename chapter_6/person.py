# 6-1. Person: Use a dictionary to store information about a person you know.  Store their first name, last name, age, and the city in which they live. You  should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary. 

Benny = {'first_name': 'Benson',
    'last_name': 'Trinidad',
    'age': 29,
    'city': 'Los Angeles'
    }

print("Benny's Information:\n")

for info in Benny:
    print(f"{info.title()}: {Benny[info]} ")

