# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do  each of the following at least once: 

# •  Use a conditional test in the while statement to stop the loop. 


toppings = ""

while toppings.lower() != 'quit':
    prompt = "Enter the pizza toppings you would like to add to your pizza."
    prompt += "\nEnter 'quit' to stop. "
  
    toppings = input(prompt)

    if toppings.lower() == 'quit':
        print("\nQuitting...")
    else:
        print(f"Adding {toppings.title()}!\n")
    
    
       

# •  Use an active variable to control how long the loop runs. 

active = True

while active:
    prompt = "Enter the pizza toppings you would like to add to your pizza."
    prompt += "\nEnter 'quit' to stop. "

    toppings = input(prompt)
    
    if toppings.lower() == 'quit':
        print("\nQuitting...")
        active = False
    else:
        print(f"Adding {toppings.title()}!\n")


# •  Use a break statement to exit the loop when the user enters a 'quit' value. 

while True:
    prompt = "Enter the pizza toppings you would like to add to your pizza."
    prompt += "\nEnter 'quit' to stop. "

    toppings = input(prompt)
    
    if toppings.lower() == 'quit':
        print("\nQuitting...")
        break
    else:
        print(f"Adding {toppings.title()}!\n")