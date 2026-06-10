# What is the Python "if" statement?
# What are conditional tests? - Expressions that can be evaluated as True or False.
# In Python, why does for loop and if statements require colon in their sytax?

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Ignoring case when checking for equality

car = "Audi"
print("\n")
print(car == "audi")
print(car.lower() == "audi")
print(car)
print("\n")

# Checking for Inequality; Use not equal operator !=

requested_topping = "mushrooms"

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print('\n')

# Numerical Comparison: Checking if two numbers are equal

age = 18
print(age == 18)
print(age != 99)
print("\n")
# Check Multiple Conditions:

# "and" both tests must be True

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >=21) #Fail; second test is false
age_1 = 25
print(age_0 >= 21 and age_1 >=21) #True; both test is true.

# "or" either one of the tests must be True

print(age >= 21 or age_1 >=21) #Evalutes to False in "AND" but TRUE in "OR"

# Check Whether: (1) A value is in a list (2) is not in a list

requested_toppings = ['mushrooms', 'onions', 'pineapple'] 
print('mushrooms' in requested_toppings) #check value in a list
print('sugar' not in requested_toppings) #check value not in a list

# Boolean Values: (1) True (2) False

