# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on  a person’s age. If a person is under the age of 3, the ticket is free; if they are  between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is  $15. Write a loop in which you ask users their age, and then tell them the cost  of their movie ticket. 


active = True

while True:
    prompt = "Welcome to Mew York Movie Theater, would you like to know the cost of one ticket?"
    prompt += "\nIf so, then all I need is your age. "
    age = int(input(prompt))
    if age < 3:
        print("Young one, your ticket is on the house!\n")
    elif age >= 3 and age <= 12:
        print("Your ticket will be ten dollars.\n") 
    elif age > 12:
        print("Your ticket will be fifteen dollars.\n")