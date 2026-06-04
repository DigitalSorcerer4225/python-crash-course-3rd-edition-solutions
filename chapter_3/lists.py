# In the context of computer science and programming, what are lists and what can you do with them?
# How are lists used in programming?
# I've read in a book that lists are supposed to tie together many important concepts in programming. How so?
# What are naming conventions of lists in Python and in any programming language in general?
# In Python, the start of a count for a list is zero and not one. Why?
# In Python, what are the different ways of accessing the elements of a list?
# In Python, how do you modify, add, and remove elements in a list?
# In Python, how do you organize a list?
# In Python, what is a statement? How is it different from a function, and a method?
# In Python, what are the common errors beginners encounter?

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("\t", bicycles[0].title())
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

bicycles[0] = 'ducati' #overites the element at the 0th position of the bicycle list
print(bicycles[0])
print(bicycles)

bicycles.append('tricycle') #adds tricycle at the end of the list of bicycles
print(bicycles)

bicycles.insert(0, 'tookati') #adds tookati at the 0th position and shifts all the elements of the list
print(bicycles)

del bicycles[0] #removes the element at the 0th position of the list bicycles. Wont be able to access the removed element.
print(bicycles)

popped_bicycle = bicycles.pop() #removes the last element of the list bicycles. Pop method allows us to use the removed element.
print(bicycles)
print(popped_bicycle)
popped_bicycle = bicycles.pop(2) #removes the 3rd element of the list bicycles. Pop method allows us to use the removed element.
print(bicycles)
print(popped_bicycle)

bicycles.remove('ducati') #removes the element: ducati in the list using its value.
print(bicycles)

#you can also work with deleted values using remove using this strategy:

too_expensive = 'specialized'
bicycles.remove(too_expensive)
print(bicycles)
print(f"\nA {too_expensive.title()} is too expensive for me.") 
