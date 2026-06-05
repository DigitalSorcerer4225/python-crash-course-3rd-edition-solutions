# Q: What are the uses of numerical lists?
# Q: Why does the list() function do and why does it allow to create a list uing list(range())
# Q: What are list comprehensions and what are they used for?


# Generate a series of numbers using the range() function:

for value in range(1,5):
    print(value)

print("\n")

for value in range(1,6):
    print(value)

print("\n")

for value in range(6):
    print(value)

print("\n")


# Using range to make a list of numbers using the list() and range() function.

numbers = list(range(1,6))
print(numbers)

# even numbers

even_numbers = list(range(2,11,2))
print(even_numbers)

# first ten square numbers:

squares = []
for value in range(1,11):
    value = value ** 2
    squares.append(value)

print(squares)


# Finding the min, max, and sum of the numbers in a list:

digits = range(10)
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension for building a list of squares:

squares = [value**2 for value in range(1,11)]
print(squares)