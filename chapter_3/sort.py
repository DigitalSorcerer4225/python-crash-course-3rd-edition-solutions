# What are the ways that you can sort a list in Python?
# Why do we have redundant commands in Python. For example the sorted function and the sort method.

cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort() #alphabetical sort; cannot reverse action
print(cars) 
cars.sort(reverse=True) #reverse-alphabetical sort; cannot reverse action
print(cars) 

cars = ['bmw', 'audi', 'toyota', 'subaru'] 
print(sorted(cars)) #sort not permanent
print(cars)

cars.reverse() #reverse-chronological order. permanent
print(cars) 

print(len(cars))