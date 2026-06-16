alien_0 = {'color': 'green', 'points': 5}

# Accessing Values in a Dictionary

new_points = alien_0['points']
print(f"You just earned {new_points} points!") 

# Adding New Key-Value pairs (Dictionaries are mutable)

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying Values in a Dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow' 
print(f"The alien is now {alien_0['color']}.")

# Removing Key-Value Pairs; use del statement
# what is a del statement and what are statements in python?

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# You can store many objects of the same kind of information. For example:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# The get() method is a method that can be used to get a specific value in a dictionary
# You can also set a default value that will be returned if the requested key does not exist.

point_value = alien_0.get('points', 'No point value assigned.')
[print(point_value)]