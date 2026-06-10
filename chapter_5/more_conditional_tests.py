# 5-2. More Conditional Tests: You don’t have to limit the number of tests you cre­ ate to 10. If you want to try more comparisons, write more tests and add them  to conditional_tests.py.


print("Condition 1: Test for Equalty and Inequality with Strings:\n")

spelling = 'sayns'
print(spelling.lower() == "science")
print(spelling.lower() != 'sceince')

spelling = 'science'
print(spelling.lower() == 'science')
print(spelling.lower() != 'science')


print("\nCondition 2: Test using the lower() method:\n")

user = 'jEjEmoN'
print(user.lower() == 'jejemon')
print(user.lower() != 'jejemon')


print("\nNumerical tests involving equality and ineqaulity, greater than and less than, greater than or equal to, and less than or equal to.")

first_number = 1
second_number = 999
print(first_number == 1)
print(first_number != second_number)
print(first_number > second_number)
print(first_number < second_number)
print(first_number >= -1)
print(second_number <= 1000)


print("\nTests using the 'AND' keyword and the 'OR' keyword.\n")

battery_on = True
print(spelling.lower() == "science" and battery_on == True)


print("\nTest whether an item is in a list:\n")

herbs_spices = ['paprika','pepper', 'oregano']
print('rosemary' in herbs_spices)
print('rosemary' not in herbs_spices)