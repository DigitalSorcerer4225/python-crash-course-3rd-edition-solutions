# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of  pizza toppings until they enter a 'quit' value. As they enter each topping, print  a message saying you’ll add that topping to their pizza. 

while True:
    prompt = "Enter the pizza toppings you would like to add to your pizza."
    prompt += "\nEnter 'quit' to stop. "

    toppings = input(prompt)
    
    if toppings.lower() == 'quit':
        break
    else:
        print(f"Adding {toppings.title()}!\n")

